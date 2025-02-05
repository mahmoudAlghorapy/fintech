from odoo import models,fields

class StockMoveInherit(models.Model):
    _inherit = 'stock.move'

    remark = fields.Text("Remark", readonly=True)

