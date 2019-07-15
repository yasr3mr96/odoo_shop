# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ShopCustomers(models.Model):
    _name = 'shop.customers'

    name = fields.Char(string="Name",required=True)
    address = fields.Char(string="Address")
    phone = fields.Char(string="Phone",size=11)
    email = fields.Char(string="Email")
    notes = fields.Html(string="Notes")
