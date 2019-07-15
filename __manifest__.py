# -*- coding: utf-8 -*-
{
    'name': "Shop Management System",

    'summary': """
        Shop Management System
        """,

    'description': """
       Shop Management System
    """,

    'author': "yasr3mr",
    'website': "http://www.facebook.com/yasr3mr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/shop_menus.xml',
        'views/shop_suppliers_view.xml',
        'views/shop_customers_view.xml',
        'views/shop_employees_view.xml',
        'views/shop_expenses_view.xml',
        'views/shop_products_view.xml',
        'views/shop_units_view.xml',
        'views/shop_purchases_view.xml',
        'views/shop_sales_view.xml',
        'views/shop_income_view.xml',
        'reports/report.xml',
        'reports/shop_suppliers_template.xml',
        'reports/shop_customers_template.xml',
        'reports/shop_employees_template.xml',
        'reports/shop_expenses_template.xml',
        'reports/shop_products_template.xml',
        'reports/shop_income_template.xml',
        'reports/shop_purchases_template.xml',
        'reports/shop_sales_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}