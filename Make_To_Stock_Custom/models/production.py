from odoo import models, fields, api

class ProductionOrder(models.Model):
    _inherit = 'mrp.production'

    def create_production_order(self):
        for product in self.env['product.product'].search([('make_to_stock', '=', True)]):
            bom = self.env['mrp.bom'].search([('product_id', '=', product.id)], limit=1)
            if bom:
                self.create({
                    'product_id': product.id,
                    'bom_id': bom.id,
                })
