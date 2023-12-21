from odoo import models, api, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    vendor_type_id = fields.Many2one("res.partner.vendor.type",
                                     string="Vendor Type",
                                     related="partner_id.vendor_type_id")
