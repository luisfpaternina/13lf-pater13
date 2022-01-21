from odoo import models, fields, api, _


class ProductProduct(models.Model):
    _inherit = 'product.product'

    codigo_ncm = fields.Char(string="Codigo NCM")





class ProductTemplate(models.Model):
    _inherit = 'product.template'

    codigo_ncm = fields.Char(string="Codigo NCM")
