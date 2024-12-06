from odoo import models, fields

class BOM(models.Model):
    _inherit = 'mrp.bom'

    product_id = fields.Many2one('product.product', string='Product')
    raw_material_line_ids = fields.One2many('bom.raw.material.line', 'bom_id', string='Raw Materials')

class BOMRawMaterialLine(models.Model):
    _name = 'bom.raw.material.line'
    _description = 'BOM Raw Material Line'

    bom_id = fields.Many2one('mrp.bom', string='BOM', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Raw Material', required=True)
    product_qty = fields.Float(string='Quantity', required=True, default=1.0)
