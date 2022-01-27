from odoo import models, fields, api, _
from datetime import datetime, date
import logging

class AccountPayment(models.TransientModel):
    _inherit = 'account.payment'