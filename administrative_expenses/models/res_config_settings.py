from odoo import fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    title_page_text = fields.Char(string='Title Page Text',
        config_parameter='certificate_planer.title_page_text',
        default="This document contains confidential information and is proprietary to Example.")
    
    footer_text = fields.Char(string='Footer Text',
        config_parameter='certificate_planer.footer_text',
        default="Copyright by Example")
