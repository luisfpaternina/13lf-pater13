from odoo import models, fields, api, _
from datetime import datetime, date
import logging

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def post(self):
        rec = super(AccountPayment, self).post()
        acc_move_obj = self.env['account.move'].search([('name','=',self.communication)],limit=1)
        if acc_move_obj:
            for record in acc_move_obj:
                if record.invoice_payments_widget:
                    logging.info("widget dateeeeeeeeeeeeeeeeeee", record.invoice_payments_widget)
                    logging.info("ENTROOOOOOOOOOOOOOOOOOOO CAUCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", record.invoice_payments_widget)
                    date_str = record.invoice_payments_widget
                    logging.info("date strrrrrrrrrrrrrrrr",date_str)
                    date_dt = datetime.strptime(date_str, '%d/%m/%Y')
                    logging.info("kkkkkkkkkkkkkkkkkkkkkkkkkkkk", date_dt)
                    date_date = date_dt.date()
                    record.register_date = date_date
                    logging.info("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                    logging.info(record.register_date)
        return rec
