from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    lead_id = fields.Many2one('crm.lead', string="Related Lead")
