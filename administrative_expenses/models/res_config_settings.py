from odoo import fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    late_charge = fields.Char(
        string="Late charge",
        default="Cargo por pago fuera de término",
        config_parameter='administrative_expenses.late_charge')
    late_charge_value = fields.Float(
        string="Late charge value",
        default=10)
    late_charge_days = fields.Integer(
        string="Late charge days",
        default=5)
    late_fee = fields.Char(
        string="Late fee",
        default="Cargo por mora")
    late_fee_value = fields.Float(
        string="Late fee value",
        default=15)
    late_fee_days = fields.Integer(
        string="Late fee days",
        default=30)
    block_name = fields.Char(
        string="Name",
        default="Costo de bloqueo modem")
    block_value = fields.Float(
        string="Value",
        default=300)
    block_rejected = fields.Char(
        string="Name",
        default="Cargo por débito rechazado")
    rejected_value = fields.Float(
        string="Value",
        default=500)
