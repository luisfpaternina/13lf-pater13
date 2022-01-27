# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime
from pytz import timezone

class SaleSuscriptionInherit(models.Model):
    _inherit = 'sale.subscription'

    def _recurring_create_invoice(self):
        res = super(SaleSuscriptionInherit, self)._recurring_create_invoice()
        for record in self:
            record._validate_subscription()
        return res