from odoo import models, fields, api, _
from datetime import datetime, date
import logging

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def create(self, vals):
        rec = super(AccountJournal, self).create(vals)
        # ...        
        return rec