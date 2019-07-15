# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ShopSuppliers(models.Model):
    _name = 'shop.suppliers'

    name = fields.Char(string="Name",required=True)
    company_name = fields.Char(string="Company Name")
    address = fields.Char(string="Address")
    phone = fields.Char(string="Phone",size=11)
    email = fields.Char(string="Email")
    website = fields.Char(string="Website")
    notes = fields.Html(string="Notes")
