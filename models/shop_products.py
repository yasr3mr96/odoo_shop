# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ShopProducts(models.Model):
    _name = 'shop.products'

    name = fields.Char(string="Name",required=True)
    barcode = fields.Char(string="Barcode",required=True)
    quantity= fields.Integer(string="Quantity", required=True)
    wholesaleprice=fields.Float(string="Wholesale Price",required=True)
    saleprice=fields.Float(string="Sale Price",required=True)
    image = fields.Binary(string="Image")
    supplier_name = fields.Many2one(comodel_name="shop.suppliers", string="Supplier Name")
    unit_name = fields.Many2one(comodel_name="shop.units", string="Unit Name")
    _sql_constraints = [
        ('barcode_uniq', 'UNIQUE (barcode)', 'You can not have two Products with the same barcode !')
    ]


