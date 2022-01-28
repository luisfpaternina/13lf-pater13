from odoo import models, fields, api, _
from datetime import datetime, date
import logging

class AccountMove(models.Model):
    _inherit = 'account.move'

    # Variables
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
        string="Payment date")
    expense_product = fields.Many2one(
        'product.template',
        string="Product",
        compute="add_administrative_expense_product")
    days_difference = fields.Integer(
        string='Days',
        compute="_compute_difference")
    expense_name = fields.Char(
        string="Expense name",
        compute="_get_expenses_names")
    is_blocking = fields.Boolean(
        string="Blocking",
        related="partner_id.is_blocking")
    register_date = fields.Date(
        string="Register date")

    
    # Función para traer la parametrización(datos) realizada en res.config.settings
    @api.depends('days_difference')
    def _get_expenses_names(self):
        settings_obj = self.env['res.config.settings'].search([])
        for record in self:
            late_charge = record.env.company.late_charge
            late_charge_value = record.env.company.late_charge_value
            late_charge_days = record.env.company.late_charge_days
            late_fee = record.env.company.late_fee
            late_fee_value = record.env.company.late_fee_value
            late_fee_days = record.env.company.late_fee_days
            if record.is_blocking:
                record.expense_name = 'Costo de bloqueo modem'
            elif record.days_difference <= 10:
                record.expense_name = late_charge
            elif record.days_difference >= 30:
                record.expense_name = late_fee
            else:
                record.expense_name = ' '


    # Función para calcular los días de mora
    @api.depends('aditional_payment_date','invoice_date_due')
    def _compute_difference(self):
        for rec in self:
            if rec.register_date and rec.invoice_date_due:
                rec.days_difference = (rec.register_date - rec.invoice_date_due).days
            else:
                rec.days_difference = 0


    # Función para traer el producto gasto administrativo el cual se carga en la data del modulo
    @api.depends('name')
    def add_administrative_expense_product(self):
        product_obj = self.env['product.template'].search([('name', '=', 'Gasto administrativo')])
        if product_obj:
            self.expense_product = product_obj.id
        else:
            self.expense_product = False


    @api.onchange(
        'aditional_payment_date',
        'invoice_date_due',
        'state',
        'invoice_payment_term_id',
        'invoice_date',
        'name')
    def _calculate_payment_date(self):
        payment_obj = self.env['account.payment'].search([('communication', '=', self.name)],limit=1)
        if payment_obj:
            self.aditional_payment_date = payment_obj.payment_date
        else:
            self.aditional_payment_date = False


    # Calculo del valor del gasto administrativo dependiendo de los días de mora
    @api.depends('register_date','invoice_date_due')
    def _calculate_aditional_value(self):
        if self.register_date and self.invoice_date_due:
            if self.register_date > self.invoice_date_due and self.days_difference < 10:
                self.aditional_value = self.amount_untaxed * 0.10
            elif self.register_date > self.invoice_date_due and self.days_difference >= 30:
                self.aditional_value = self.amount_untaxed * 0.15
            else:
                self.aditional_value = 0.0
        else:
            self.aditional_value = 0.0


    # Función para comparar fechas: fecha de pago vs plazo de pago
    @api.depends(
        'register_date',
        'invoice_date_due',
        'state',
        'invoice_payment_term_id',
        'invoice_date',
        'name')
    def _validate_dates(self):
        for record in self:
            if record.register_date and record.invoice_date_due:
                if record.register_date > record.invoice_date_due:
                    record.is_validate_date = True
                elif record.register_date <= record.invoice_date_due:
                    record.is_validate_date = False
                else:
                    record.is_validate_date = False
            else:
                record.is_validate_date = False


    # Función para agregar o eliminar líneas en la suscripción dependiendo el gasto administrativo
    def _validate_subscription(self):
        for record in self:
            if record.invoice_payment_state == 'paid' and record.is_blocking:
                sale_obj = record.env['sale.order'].search([('name', '=', record.invoice_origin)])
                subscription_obj = record.env['sale.subscription'].search([])
                logging.info("BLOCKINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
                logging.info(subscription_obj)
                for s in subscription_obj:
                    if sale_obj:
                        record.is_validate = True
                        if s in sale_obj.order_line.subscription_id:
                            s.display_name
                            c = 1
                            for line in s.recurring_invoice_line_ids:
                                range_number = len(s.recurring_invoice_line_ids)
                                if c < range_number:
                                    quantity = 1
                                    price_unit = 0
                                else:
                                    quantity = 1
                                    price_unit = 300

                                vals = {
                                    'product_id': record.expense_product.id,
                                    'name': record.expense_name,
                                    'price_unit': price_unit,
                                    'quantity': quantity,
                                    'uom_id': s.recurring_invoice_line_ids.uom_id.id,
                                    }
                                line.write(vals)
                                c = c + 1
                            break
                        else:
                            record.is_validate = False
                    else:
                        record.is_validate = False
            elif record.invoice_payment_state == 'paid' and record.is_validate_date:
                sale_obj = record.env['sale.order'].search([('name', '=', record.invoice_origin)])
                subscription_obj = record.env['sale.subscription'].search([])
                logging.info("GASTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                logging.info(subscription_obj)
                for s in subscription_obj:
                    logging.info("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
                    if sale_obj:
                        record.is_validate = True
                        if s in sale_obj.order_line.subscription_id:
                            s.display_name
                            if len(s.recurring_invoice_line_ids) < 2:
                                vals = {
                                'recurring_invoice_line_ids': [(0, 0, {
                                    'product_id': record.expense_product.id,
                                    'name': record.expense_name,
                                    'price_unit': record.aditional_value,
                                    'quantity': 1,
                                    'uom_id': s.recurring_invoice_line_ids.uom_id.id,
                                    })]
                                }
                                s.write(vals)
                                break
                            else:
                                record.is_validate = False
                        else:
                            record.is_validate = False
                    else:
                        record.is_validate = False
            elif record.invoice_payment_state == 'paid' and record.is_validate_date == False:
                logging.info("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                sale_obj = record.env['sale.order'].search([('name', '=', record.invoice_origin)])
                subscription_obj = record.env['sale.subscription'].search([])
                for s in subscription_obj:
                    if sale_obj:
                        record.is_validate = True
                        if s in sale_obj.order_line.subscription_id:
                            s.display_name
                            for sus_line in s.recurring_invoice_line_ids:
                                logging.info("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
                                if sus_line.product_id.name == 'Gasto administrativo':
                                    logging.info("....................................................................")
                                    sus_line.unlink()
                                    logging.info("00000000000000000000000000000000000000000000payr")
                                    record.is_validate = False
                                else:
                                    record.is_validate = False
                        else:
                            record.is_validate = False
                    else:
                        record.is_validate = False
            else:
                record.is_validate = False
