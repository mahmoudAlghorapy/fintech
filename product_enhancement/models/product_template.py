# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import random
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'



    arabic_name = fields.Char(string='Arabic Name', required=False)
    type_category = fields.Selection([
        ('spare_parts', 'Spare Parts'),
        ('equipment', 'Equipment')
    ], string='Type')
    sub_categ_id = fields.Many2one(
        'product.category', string='Sub Catergories', domain="[('parent_id', '!=', False)]")
    has_warranty = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ], string='Has Warranty?', default='no')
    brand_id = fields.Many2one('product.brand', string="Brand")
    model_id = fields.Many2one('product.model', string="Model")
    country_id = fields.Many2one('res.country', string='Country Origin',
                                 help="Apply only if delivery country matches.")
    part_number_source = fields.Text(
        string="Part Number with Source",
        help="Stores part numbers and their sources in a text format."
    )
    detailed_type = fields.Selection(default='product')

    # barcode = fields.Char(
    #     'Barcode', copy=False, compute='_compute_barcode',
    #     help="International Article Number used for product identification.")
    # analytic_account_id = fields.Many2one("account.analytic.account", string="Analytic Account",
    #                                       related="categ_id.analytic_account_id")
    # default_code = fields.Char('Internal Reference', compute='_compute_default_code', store=True)
    # type = fields.Selection([
    #     ('consu', 'Consumable'),
    #     ('service', 'Service'), ('product', 'Storable Product')], string='Product Type', default='product',
    #     required=True,
    #     help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
    #          'A consumable product is a product for which stock is not managed.\n'
    #          'A service is a non-material product you provide.')
    #
    # @api.depends('barcode')
    # def _compute_default_code(self):
    #     for rec in self:
    #         rec.default_code = rec.barcode
    #
    # @api.depends('template_code', 'categ_id.barcode')
    # def _compute_barcode(self):
    #     for product in self:
    #
    #         if product.categ_id.barcode and product.template_code:
    #             product.barcode = f"{product.categ_id.barcode}{product.template_code}"
    #         elif product.categ_id.barcode:
    #             product.barcode = product.categ_id.barcode
    #         elif product.template_code:
    #             product.barcode = product.template_code
    #
    #         else:
    #             product.barcode = False