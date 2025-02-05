# -*- coding: utf-8 -*-
{
    'name': "sale Enhancement",
    'category': 'sale',
    'version': '17.0',
    'depends': ['base','sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'reports/sale_report.xml',
        'reports/sale_template.xml',
        'views/sale_view.xml',
        # 'views/product_views.xml',

        # 'wizard/sale_coupon_apply_code_views.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
