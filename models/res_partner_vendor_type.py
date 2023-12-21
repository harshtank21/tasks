from odoo import models, fields, api


class ResPartnerVendorType(models.Model):
    _name = "res.partner.vendor.type"
    _description = "tasks"

    description = fields.Char(string="Description")
    name = fields.Char(string="Vendor Type")
    active = fields.Boolean(default=True)

