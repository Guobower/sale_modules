# -*- coding: utf-8 -*-

import requests
import json

from odoo import models, api, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def do_email_validation_request(self, access_key, email):
        payload = {
            'access_key': access_key,
            'email': email,
        }
        response = requests.get("https://apilayer.net/api/check", params=payload)
        response.raise_for_status()
        parsed_json_dict = json.loads(response.content)
        return parsed_json_dict["format_valid"]

    @api.multi
    def mail_validator(self):
        mailboxlayer_access_key = self.env['ir.config_parameter'].get_param(
            'partner_email_validator.mailboxlayer_access_key'
        )
        for partner in self:
            if partner.email:
                result = self.do_email_validation_request(mailboxlayer_access_key, partner.email)
                if result:
                    raise UserError(_('Email is valid!'))
                else:
                    raise UserError(_('Email is Invalid!'))
            else:
                raise UserError(_('Email is empty!'))
