from odoo import fields, models, api, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    late_charge = fields.Char(
        string="Late charge",
        related="company_id.late_charge",
        readonly=False,
        config_parameter='admministrative_expenses.late_charge')
    late_charge_value = fields.Float(
        string="Late charge value",
        related="company_id.late_charge_value",
        readonly=False,
        config_parameter='admministrative_expenses.late_charge_value')
    late_charge_days = fields.Integer(
        string="Late charge days",
        related="company_id.late_charge_days",
        readonly=False,
        config_parameter='admministrative_expenses.late_charge_days')
    late_fee = fields.Char(
        string="Late fee",
        related="company_id.late_fee",
        readonly=False,
        config_parameter='admministrative_expenses.late_fee')
    late_fee_value = fields.Float(
        string="Late fee value",
        related="company_id.late_fee_value",
        readonly=False,
        config_parameter='admministrative_expenses.late_fee_value')
    late_fee_days = fields.Integer(
        string="Late fee days",
        related="company_id.late_fee_days",
        readonly=False,
        config_parameter='admministrative_expenses.late_fee_days')
    block_name = fields.Char(
        string="Name",
        related="company_id.block_name",
        readonly=False,
        config_parameter='admministrative_expenses.block_name')
    block_value = fields.Float(
        string="Value",
        related="company_id.block_value",
        readonly=False,
        config_parameter='admministrative_expenses.block_value')
    block_rejected = fields.Char(
        string="Name",
        default="Cargo por débito rechazado",
        config_parameter='admministrative_expenses.block_rejected')
    rejected_value = fields.Float(
        string="Value",
        default=500,
        config_parameter='admministrative_expenses.rejected_value')

    """
    @api.model
    def get_default_expenses_values(self, fields):
        conf = self.env['ir.config_parameter']
        return {
            'late_charge': conf.get_param('admministrative_expenses.late_charge'),
            'late_fee': conf.get_param('admministrative_expenses.late_fee'),
            'late_charge_value': conf.get_param('admministrative_expenses.late_charge_value'),
        }

    def set_expenses_values(self):
        conf = self.env['ir.config_parameter']
        conf.set_param('admministrative_expenses.late_charge', self.late_charge)
        conf.set_param('admministrative_expenses.late_fee', self.late_fee)
        conf.set_param('admministrative_expenses.late_fee', self.late_charge_value)
    """


    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('late_fee', self.late_fee)
        return res
