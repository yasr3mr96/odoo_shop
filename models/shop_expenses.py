# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ShopExpenses(models.Model):
    _name = 'shop.expenses'

    name = fields.Char(string="Name",required=True)
    value = fields.Float(string="Value", required=True)
    date = fields.Datetime(string="Date", required=True)
    notes = fields.Html(string="Notes")

