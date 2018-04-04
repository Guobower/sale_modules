# -*- coding: utf-8 -*-

import datetime

from odoo import models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def send_weekly_sales_mail(self):
        template = self.env.ref('weekly_sales_report.weekly_sale_email_template')
        sales_data = []
        today = datetime.date.today()
        today_number = (today.weekday() + 1) % 7  # MON = 0, SUN = 6 -> SUN = 0 .. SAT = 6
        sun = (today - (datetime.timedelta(7 + today_number))).strftime('%Y-%m-%d 00:00:00')
        sat = (today - (datetime.timedelta(7 + today_number - 6))).strftime('%Y-%m-%d 23:59:59')
        orders = self.search([('confirmation_date', '>=', sun), ('confirmation_date', '<=', sat)])
        for order in orders:
            line_data = {
                'name': order.name,
                'total': order.amount_total,
                'tax': order.amount_tax,
            }
            sales_data.append(line_data)
        template.with_context(sales_data=sales_data).send_mail(self.id, force_send=True, raise_exception=True)
