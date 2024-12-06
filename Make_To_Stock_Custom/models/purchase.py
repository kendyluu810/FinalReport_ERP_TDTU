from odoo import models, fields, api
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def create_purchase_order(self):
        """
        Create purchase orders for raw materials required in Make-To-Stock process.
        """
        # Get all products marked as Make-To-Stock
        make_to_stock_products = self.env['product.product'].search([('make_to_stock', '=', True)])

        for product in make_to_stock_products:
            # Get BOM (Bill of Materials) for the product
            bom = self.env['mrp.bom'].search([('product_tmpl_id', '=', product.product_tmpl_id.id)], limit=1)
            if not bom:
                raise UserError(f"No BOM found for product {product.name}.")

            for line in bom.bom_line_ids:
                # Get the supplier for the raw material
                raw_material = line.product_id
                supplier_info = self.env['product.supplierinfo'].search([
                    ('product_tmpl_id', '=', raw_material.product_tmpl_id.id)
                ], limit=1)

                if not supplier_info:
                    raise UserError(f"No supplier found for raw material {raw_material.name}.")

                # Create a purchase order line
                purchase_order = self.create({
                    'partner_id': supplier_info.name.id,  # Supplier
                    'date_order': fields.Date.today(),
                    'order_line': [(0, 0, {
                        'product_id': raw_material.id,
                        'product_qty': line.product_qty,
                        'product_uom': raw_material.uom_id.id,
                        'price_unit': supplier_info.price,
                        'date_planned': fields.Date.today(),
                    })],
                })
                self.message_post(body=f"Purchase Order created for raw material: {raw_material.name}")
