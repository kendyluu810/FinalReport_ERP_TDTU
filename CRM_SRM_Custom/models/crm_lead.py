from odoo import models, fields

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    lead_score = fields.Integer(string='Lead Score', default=0)
    supplier_needed = fields.Boolean(string='Supplier Needed', default=False)

    def action_create_supplier_order(self):
        for lead in self:
            if lead.supplier_needed:
                purchase_order = self.env['purchase.order'].create({
                    'partner_id': lead.partner_id.id,
                    'date_order': fields.Datetime.today(),
                    'order_line':[(0, 0,{
                        'product_id': lead.product_id.id,
                        'product_qty': 1,
                    })]
                })
                lead.message_post(body="Purchase Order Created Based On This Lead.")