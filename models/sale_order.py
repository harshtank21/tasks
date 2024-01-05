from odoo import models, fields, api


class SaleOrderEmail(models.Model):
    _inherit = "sale.order"
    send_email = fields.Boolean(string="Sand Email")


class EmailSender(models.TransientModel):
    _inherit = "mail.compose.message"

    def action_send_mail(self):
        store = self.env["sale.order"].browse(self.res_id)
        store.send_email = True
        
        return super().action_send_mail()
