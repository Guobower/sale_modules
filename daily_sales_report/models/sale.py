# -*- coding: utf-8 -*-

import datetime

from odoo import models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def send_daily_sales_mail(self):
        template = self.env.ref('daily_sales_report.daily_sale_email_template')
        sales_data = []
        start_datetime = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')
        stop_datetime = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d 23:59:59')
        orders = self.search([('confirmation_date', '>=', start_datetime), ('confirmation_date', '<=', stop_datetime)])
        for order in orders:
            line_data = {
                'name': order.name,
                'total': order.amount_total,
                'tax': order.amount_tax,
            }
            sales_data.append(line_data)
        template.with_context(sales_data=sales_data).send_mail(self.id, force_send=True, raise_exception=True)
