from odoo import models, fields, api, _
from datetime import datetime
from datetime import date
import logging

class AccountMove(models.Model):
    _inherit = 'account.move'

    is_validate = fields.Boolean(
        string="Validate",
        compute="_validate_subscription")
    is_validate_date = fields.Boolean(
        string="Validate dates",
        compute="_validate_dates")
    aditional_value = fields.Float(
        string="Aditional value",
        compute="_calculate_aditional_value")
    aditional_payment_date = fields.Date(
        string="Payment date",
        compute="_calculate_payment_date")
    expense_product = fields.Many2one(
        'product.template',
        string="Product",
        compute="add_administrative_expense_product")
    days_difference = fields.Integer(
        string='Days',
        compute="_compute_difference")


    @api.depends('aditional_payment_date','invoice_date_due')
    def _compute_difference(self):
        for rec in self:
            if rec.aditional_payment_date and rec.invoice_date_due:
                rec.days_difference = (rec.aditional_payment_date - rec.invoice_date_due).days
            else:
                rec.days_difference = 0


    @api.depends('name')
    def add_administrative_expense_product(self):
        product_obj = self.env['product.template'].search([('name', '=', 'Gasto administrativo')])
        if product_obj:
            self.expense_product = product_obj.id
        else:
            self.expense_product = False


    def _calculate_payment_date(self):
        payment_obj = self.env['account.payment'].search([('communication', '=', self.name)],limit=1)
        if payment_obj:
            self.aditional_payment_date = payment_obj.payment_date
        else:
            self.aditional_payment_date = False


    @api.depends('aditional_payment_date','invoice_date_due')
    def _calculate_aditional_value(self):
        if self.aditional_payment_date and self.invoice_date_due:
            logging.info("DATESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
            if self.aditional_payment_date > self.invoice_date_due and self.days_difference < 10:
                self.aditional_value = self.amount_untaxed * 0.10
                logging.info("VALUE-UNOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
            elif self.aditional_payment_date > self.invoice_date_due and self.days_difference >= 30:
                self.aditional_value = self.amount_untaxed * 0.15
                logging.info("VALUE-DOSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
            else:
                self.aditional_value = 0.0
        else:
            self.aditional_value = 0.0


    @api.depends('aditional_payment_date','invoice_date_due')
    def _validate_dates(self):
        if self.aditional_payment_date and self.invoice_date_due:
            if self.aditional_payment_date > self.invoice_date_due:
                self.is_validate_date = True
            else:
                self.is_validate_date = False
        else:
            self.is_validate_date = False


    def _validate_subscription(self):
        for record in self:
            if record.invoice_payment_state == 'paid' and record.is_validate_date:
                sale_obj = record.env['sale.order'].search([('name', '=', record.invoice_origin)])
                subscription_obj = record.env['sale.subscription'].search([])
                logging.info("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                logging.info(subscription_obj)
                for s in subscription_obj:
                    if sale_obj:
                        record.is_validate = True
                        if s in sale_obj.order_line.subscription_id:
                            s.display_name
                            logging.info("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                            logging.info(s.display_name)
                            vals = {
                            'partner_id': s.partner_id.id,
                            'recurring_invoice_line_ids': [(0, 0, {
                                'product_id': record.expense_product.id,
                                'name': 'Cargo por pago fuera de término',
                                'price_unit': record.aditional_value,
                                'quantity': 1,
                                'uom_id': s.recurring_invoice_line_ids.uom_id.id,
                                })]
                            }
                            logging.info("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
                            logging.info(vals)
                            s.write(vals)
                            break
                    else:
                        record.is_validate = False
            else:
                record.is_validate = False
