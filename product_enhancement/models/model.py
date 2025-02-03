from odoo import models, fields

class ProductBrand(models.Model):
    _name = 'product.model'
    _description = 'Product Brand'

    name = fields.Char(string="Brand Name", required=True)
    description = fields.Text(string="Description")
