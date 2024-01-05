from odoo import models, fields, api


class CrmTask(models.Model):
    _inherit = "crm.stage"
    is_quote_ready_stage = fields.Boolean(string="Is Quote Ready Stage")


