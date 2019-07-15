# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
from odoo.exceptions import ValidationError


class ShopSales(models.Model):
    _name = 'shop.sales'

    name = fields.Char(string="Name",required=True)
    date = fields.Datetime(string="Date", required=True,default=datetime.datetime.now())
    customer_name = fields.Many2one(comodel_name="shop.customers", string="Customer Name")
    products = fields.One2many(comodel_name="shop.sales.line", inverse_name="sales_id", string="Products", required=True)

    @api.model
    def create(self, values):
        res = super(ShopSales, self).create(values)
        for i in res.products:
            prod = self.env['shop.products'].search([('id', '=', i.product_id.id)])
            prod.write({'quantity': prod.quantity - i.quantity})
            self.env['shop.income'].create({'product_id':i.product_id.id,'value':i.totals,'date':res.date})
        return res

class ShopPurchacesLine(models.Model):
    _name="shop.sales.line"
    product_id = fields.Many2one(comodel_name="shop.products", string="Product Name", required=True)
    quantity = fields.Integer(string="Quantity", required=True)
    price = fields.Float(string="Unit Price", readonly=True,related="product_id.saleprice")
    sales_id = fields.Many2one(comodel_name="shop.sales")
    totals = fields.Float(string="Total", compute="_calc_total")

    @api.onchange('quantity')
    def _onchange_product_id(self):
        if self.product_id.quantity < self.quantity:
            raise ValidationError("quantity is not enough")

    @api.one
    @api.depends('product_id', 'quantity')
    def _calc_total(self):
        self.totals = self.price * self.quantity
