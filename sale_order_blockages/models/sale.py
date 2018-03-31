# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    highrisk_country = fields.Boolean('High Risk Country')
    blacklist_status = fields.Selection([('checked', 'Checked'),
                                         ('pending', 'Pending'),
                                         ('bank_statement_requested', 'Bank Statement Requested'),
                                         ('credit_card_image_requested', 'Credit Card Image Requested')],
                                        string='Blacklist Status', track_visibility='onchange')

    @api.multi
    def action_confirm(self):
        for order in self:
            if order.blacklist_status and order.blacklist_status in ['pending',
                                                                     'bank_statement_requested',
                                                                     'credit_card_image_requested']:
                raise UserError(_('This order is Blacklisted. Please resolve it!'))
        super(SaleOrder, self).action_confirm()
