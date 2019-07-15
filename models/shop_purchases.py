# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
class ShopPurchases(models.Model):
    _name = 'shop.purchases'

    name = fields.Char(string="Name",required=True)
    date = fields.Datetime(string="Date", required=True,default=datetime.datetime.now())
    supplier_name = fields.Many2one(comodel_name="shop.suppliers", string="Supplier Name")
    products = fields.One2many(comodel_name="shop.purchases.line", inverse_name="purchases_id", string="Products", required=True)

    @api.model
    def create(self, values):
        res=super(ShopPurchases, self).create(values)
        for i in res.products:
            prod=self.env['shop.products'].search([('id','=',i.product_id.id)])
            prod.write({'quantity':prod.quantity+i.quantity})
        return res


class ShopPurchasesLine(models.Model):
    _name="shop.purchases.line"
    product_id = fields.Many2one(comodel_name="shop.products", string="Product Name", required=True)
    quantity = fields.Integer(string="Quantity", required=True)
    purchases_id = fields.Many2one(comodel_name="shop.purchases")

