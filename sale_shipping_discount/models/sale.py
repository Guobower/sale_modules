# -*- coding: utf-8 -*-

from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def discount_shipping_lines(self):
        self.ensure_one()
        shipping_lines = self.order_line.filtered(lambda line: line.is_delivery)
        shipping_discount_lines = shipping_lines.copy(default={'order_id': self.id})
        for line in shipping_discount_lines:
            line.price_unit *= -1
            line.name = 'Shipping Discount'
