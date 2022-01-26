# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountAdministrativeParameters(models.Model):
    _name = 'administrative.parameters'
    _inherit = 'mail.thread'
    _description = 'Administrative parameters'


    name = fields.Char(
        string="Name")
    active = fields.Boolean(
        string="Active")