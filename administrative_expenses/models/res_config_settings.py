from odoo import fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    title_page_text = fields.Char(
        string='Title Page Text',
        config_parameter='certificate_planer.title_page_text',
        default="This document contains confidential information and is proprietary to Example.")
    footer_text = fields.Char(
        string='Footer Text',
        config_parameter='certificate_planer.footer_text',
        default="Copyright by Example")
    late_charge = fields.Char(
        string="Late charge")
    late_charge_value = fields.Float(
        string="Late charge value")
    late_charge_days = fields.Integer(
        string="Late charge days")
    late_fee = fields.Char(
        string="Late fee")
    late_fee_value = fields.Float(
        string="Late fee value")
    late_fee_days = fields.Integer(
        string="Late fee days")
