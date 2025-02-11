
from odoo import api, fields, models, _
from num2words import num2words

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_address = fields.Char(string='Delivery address')
    amount_in_words = fields.Char(string='Amount in Words', compute='_compute_amount_in_words')
    amount_in_words_arabic = fields.Char(string='Amount in Words (Arabic)', compute='_compute_amount_in_words')
    total_subtotal = fields.Float(string="",  required=False, compute='compute_total_subtotal')
    has_warranty = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ], string='Has Warranty?',)
    delivery_date = fields.Text(string="Delivery Date", required=False, )
    barcode = fields.Char(string='Barcode', compute='_compute_barcode', copy=False)
    def action_print_quotation_report(self):
        return self.env.ref('sales_enhancement.sale_order_quotations_report').report_action(self)


    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals.update({
            'sale_order_id': self.id,
        })
        return invoice_vals


    @api.depends('order_line')
    def compute_total_subtotal(self):
        for rec in self:
            rec.total_subtotal = sum(rec.order_line.mapped('price_subtotal'))

    @api.depends('name')
    def _compute_barcode(self):
        for order in self:
            # Example: generating barcode from the order name (reference)
            order.barcode = 'BAR' + str(order.id)  # You can customize this pattern as needed



    @api.model
    def convert_to_arabic(self, number):
        arabic_numerals = {'0': '٠', '1': '١', '2': '٢', '3': '٣', '4': '٤', '5': '٥', '6': '٦', '7': '٧', '8': '٨',
                           '9': '٩', '/': '/', 'Qatar': 'قطر'}
        result = ''.join(arabic_numerals.get(digit, digit) for digit in str(number))
        print(f"Original: {number}, Converted: {result}")
        return result

    total_discount = fields.Float(
        string='Total Discount',
        compute='_compute_total_discount',
        store=True,
    )

    @api.depends('order_line.discount', 'order_line.price_unit',
                 'order_line.product_uom_qty')
    def _compute_total_discount(self):
        for order in self:
            total_discount = sum(
                (line.discount / 100) * line.product_uom_qty * line.price_unit for line in order.order_line
            )
            order.total_discount = total_discount


    @api.depends('amount_total', 'currency_id')
    def _compute_amount_in_words(self):
        for record in self:
            # Get the currency information
            currency_name = record.currency_id.full_name if record.currency_id.full_name else ''
            subunit_label = record.currency_id.currency_subunit_label if record.currency_id.currency_subunit_label else ''
            currency_translation = {
                'Qatari riyal': ' ريال قطري',
                'Egyptian pound': ' ريال قطري',
                'US Dollar': 'الدولار الأمريكي',
                'Euro': 'اليورو',
                # Add other currencies as needed
            }
            currency_name_arabic = currency_translation.get(currency_name, currency_name)

            # Convert amount_total to words
            amount_in_words = num2words(record.amount_total, lang='en').title()
            try:
                amount_in_words_ar = num2words(round(record.amount_total, 2), lang='ar')
            except NotImplementedError:
                amount_in_words_ar = "ترجمة الأرقام غير متاحة"

            # Include currency information based on whether there are decimals or not
            if '.' in str(record.amount_total):
                record.amount_in_words = f'Only {amount_in_words} {currency_name}.'
                record.amount_in_words_arabic = f" {amount_in_words_ar}{currency_name_arabic} فقط"
            else:
                record.amount_in_words = f'Only {amount_in_words} {currency_name} {subunit_label}.'
                record.amount_in_words_arabic = f" {amount_in_words_ar}{currency_name_arabic}{subunit_label} فقط"



