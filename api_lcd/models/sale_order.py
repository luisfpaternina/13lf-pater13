from odoo import models, fields, api, _

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    entrega_tienda = fields.Integer("Entrega en tienda?")
