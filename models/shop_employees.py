# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ShopEmployees(models.Model):
    _name = 'shop.employees'

    name = fields.Char(string="Name",required=True)
    salary = fields.Float(string="Salary")
    address = fields.Char(string="Address")
    phone = fields.Char(string="Phone",size=11)
    email = fields.Char(string="Email")
    notes = fields.Html(string="Notes")