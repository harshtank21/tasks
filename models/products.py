from odoo import models, api, fields


class product_tempalet(models.Model):
    _inherit = "product.category"

    office_furniture = fields.Boolean(string="Office furniture")


class sale_order_ONE(models.Model):
    _inherit = "product.template"

    brand_name = fields.Char(string="Brand")
    unique = fields.Char(string="Unique Code", compute='_compute_unique',readonly=False)
    family_name = fields.Char(string="Family Name")
    date_s = fields.Date(string="Start Date")
    truee = fields.Boolean(string="hello")

    @api.depends_context('company')
    @api.depends('product_variant_ids', 'product_variant_ids.standard_price')
    def _compute_unique(self):
        # if len(self.attribute_line_ids.value_ids) > 1:
        #     self.truee = True
        # Depends on force_company context because standard_price is company_dependent
        # on the product_product
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.unique = template.product_variant_ids.unique
            self.truee  = False
        for template in (self - unique_variants):
            template.unique = 0.0
            self.truee = True

    # def _compute_unique(self):

    # def _inverse_unique(self):
    #     for template in self:
    #         if len(template.product_variant_ids) == 1:
    #             template.product_variant_ids.unique = template.unique
    @api.model
    def _name_search(self, name="", args=None, operator='like', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        domain = [('gender', operator, "male")]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

    # @api.model
    # def name_get(self):
    #     res = []
    #     for record in self:
    #         name = record.name
    #         print(name)
    #         default_codes = record.default_code
    #         if record.categ_id.office_furniture == True and default_codes != False:
    #             name = "[ABC_" + record.default_code + "]" + name
    #         res.append((record.id, name))
    #     return res

    # @api.model
    # def name_get(self):
    #     if self._context.get('code_match'):
    #         res = []
    #         for record in self:
    #             name = record.name
    #             default_codes = record.default_code
    #             if record and default_codes:
    #                 name = "[ABC_" + record.default_code + "]" + name
    #             res.append((record.id, name))
    #         return res

    def search_read_group(self):
        self.search_read_group()

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        print(fields, "-------------->")
        return super(sale_order_ONE, self).read_group(domain, fields, groupby, offset, limit, orderby, lazy)

    def write(self, vals):
        print(self)
        if len(self.attribute_line_ids) == 0:
            vals["truee"] = False
        res = super(sale_order_ONE, self).write(vals)
        return res


class EmailSender(models.TransientModel):
    _inherit = "mail.compose.message"

    def action_send_mail(self):
        store = self.env["sale.order"].browse(self.res_id)
        store.send_email = True


# class AttributeModel(models.Model):
#     _inherit = "product.template.attribute.line"
#
#     truee = fields.Boolean(string="truee")
#
#     @api.model
#     def create(self, vals):
#         leads = super(AttributeModel, self).create(vals)
#         if len(leads.value_ids) > 1:
#             id = leads.id
#             # print(id)
#             store = self.env["product.template"].attribute_line_ids.browse(id)
#
#             # store = self.env["product.template"].search([("attribute_line_ids", "in", leads.id)])
#             store.truee = True
#         return leads
#
#     def write(self, vals):
#         res = super(AttributeModel, self).write(vals)
#         if len(self.value_ids) == 1:
#             # store = self.env["product.template"].search([("attribute_line_ids", "in", self.id)])
#             store = self.env["product.template"].attribute_line_ids.browse(self.id)
#             print(store)
#             store.truee = False
#         elif len(self.value_ids) > 1:
#             # store = self.env["product.template"].browse(self.id)
#             store = self.env["product.template"].attribute_line_ids.browse(self.id)
#             store.truee = True
#
#         return res
