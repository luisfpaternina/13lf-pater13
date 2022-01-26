from odoo import fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    title_page_text = fields.Char(
        string='Title Page Text',
        config_parameter='certificate_planer.title_page_text')
    footer_text = fields.Char(
        string='Footer Text',
        config_parameter='certificate_planer.footer_text')
    late_charge = fields.Char(
        string="Late charge",
        default="Cargo por pago fuera de término")
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
