# -*- coding: utf-8 -*-

from odoo import models, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_confirm(self):
        for order in self:
            if order.partner_id.on_hold:
                raise UserError(_('This customer is on hold. Please remove it and confirm again'))
        super(SaleOrder, self).action_confirm()
