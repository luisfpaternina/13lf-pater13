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
    valite = fields.Char(
        string="Validate",
        default="1")

    _sql_constraints = [
        ('validate_uniq', 'unique (valite)','You can add one record in this model!')
    ]