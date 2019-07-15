# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ShopIncome(models.Model):
    _name = 'shop.income'

    product_id = fields.Many2one(comodel_name="shop.products", string="Product Name", required=True)
    value = fields.Float(string="Value", readonly=True)
    date = fields.Datetime(string="Date",readonly=True)
