# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ShopUnits(models.Model):
    _name = 'shop.units'

    name = fields.Char(string="Name",required=True)
