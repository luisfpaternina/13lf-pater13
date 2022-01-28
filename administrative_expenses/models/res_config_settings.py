from odoo import fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    late_charge = fields.Char(
        string="Late charge",
        default="Cargo por pago fuera de término")
    late_charge_value = fields.Float(
        string="Late charge value",
        default=10)
    late_charge_days = fields.Integer(
        string="Late charge days")
    late_fee = fields.Char(
        string="Late fee")
    late_fee_value = fields.Float(
        string="Late fee value")
    late_fee_days = fields.Integer(
        string="Late fee days")
    block_name = fields.Char(
        string="Name")
    block_value = fields.Float(
        string="Value")
