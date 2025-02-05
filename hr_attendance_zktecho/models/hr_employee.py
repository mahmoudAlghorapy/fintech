from odoo import api, fields, models, exceptions, _


class HrEmployee_inherit(models.Model):
    _inherit = 'hr.employee'
    employee_id = fields.Char('ID', default='New', store=True)