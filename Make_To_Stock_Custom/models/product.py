from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    make_to_stock = fields.Boolean(string='Make to Stock', default=False)
