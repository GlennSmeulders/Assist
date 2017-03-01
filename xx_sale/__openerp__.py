# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'xx_sale',
    'author': "DCBO",
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Quotations, Sales Orders',
    'description': """
Sale order
==================================

* Updated sale order pdf
* Updated quotation pdf
* Price calculation based on delivered quantity
    """,
    'depends': ['sale'],
    'data': [
        'views/report_quotation.xml',
        'views/report_saleorder.xml',
        'sale_report.xml',
        'quotation_report.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
