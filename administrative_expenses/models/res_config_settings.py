from odoo import fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    late_charge = fields.Char(
        string="Late charge")
    late_charge_value = fields.Float(
        string="Late charge value",
        related="company_id.late_charge_value")
    late_charge_days = fields.Integer(
        string="Late charge days")
    late_fee = fields.Char(
        string="Late fee",
        related="company_id.late_fee")
    late_fee_value = fields.Float(
        string="Late fee value",
        related="company_id.late_fee_value")
    late_fee_days = fields.Integer(
        string="Late fee days",
        related="company_id.late_fee_days")
    block_name = fields.Char(
        string="Name",
        related="company_id.block_name")
    block_value = fields.Float(
        string="Value",
        related="company_id.block_value")
