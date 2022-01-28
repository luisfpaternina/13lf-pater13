from odoo import models, fields, api, _

class ResCompany(models.Model):
    _inherit = 'res.company'

    title_page_text = fields.Char(
        string='Title Page Text',
        config_parameter='certificate_planer.title_page_text')
    footer_text = fields.Char(
        string='Footer Text',
        config_parameter='certificate_planer.footer_text')
    late_charge = fields.Char(
        string="Late charge")
    late_charge_value = fields.Float(
        string="Late charge value")
    late_charge_days = fields.Integer(
        string="Late charge days")
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
        string="Name")
    block_value = fields.Float(
        string="Value")
