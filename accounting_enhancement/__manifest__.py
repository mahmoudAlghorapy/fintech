# -*- coding: utf-8 -*-
{
    'name': "Accounting Enhancement",
    'category': 'account',
    'version': '17.0',
    'depends': ['base','account','sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_move.xml',
        'reports/invoice_report.xml',
        'reports/invoice_template.xml',

        # 'views/product_views.xml',

        # 'wizard/sale_coupon_apply_code_views.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
