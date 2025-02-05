from odoo import models,fields

class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    barcode = fields.Char(string='Barcode', compute='_compute_barcode', copy=False)

