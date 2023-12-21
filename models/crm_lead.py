from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = "crm.lead"

    import_quote_status = fields.Selection(
        [('import_quote_requested', 'Import Quote Requested'),
         ('import_quote_ready', 'Import Quote Ready'),
         ('import_quote_submitted', 'Import Quote Submitted'),
         ('import_quote_revision_requested', 'Import Quote Revision Requested')],
        string='Import Quote Status')
    domestic_quote_status = fields.Selection(
        [('domestic_quote_requested', 'Domestic Quote Requested'),
         ('domestic_quote_ready', 'Domestic Quote Ready'),
         ('domestic_quote_submitted', 'Domestic Quote Submitted'),
         ('domestic_quote_revision_requested', 'Domestic Quote Revision Requested')],
        string="Domestic Quote Status")

    @api.onchange("domestic_quote_status", "import_quote_status")
    def _onchange_one(self):
        if not self.domestic_quote_status:
            if self.import_quote_status == "import_quote_ready":
                self.stage_id = self.env["crm.stage"].search([("name", "=", "Quote Ready")])

        elif not self.import_quote_status:
            if self.domestic_quote_status == "domestic_quote_ready":
                self.stage_id = self.env["crm.stage"].search([("is_quote_ready_stage", "=", True)])

        elif self.import_quote_status == "import_quote_ready":
            if self.domestic_quote_status == "domestic_quote_ready":
                self.stage_id = self.env["crm.stage"].search([("is_quote_ready_stage", "=", True)])



