# -*- coding: utf-8 -*-
{
    'name': "stock Enhancement",
    'category': 'stock',
    'version': '17.0',
    'depends': ['base','stock'],
    'data': [
        # 'security/ir.model.access.csv',
        'reports/delivery_report.xml',
        'reports/delivery_template.xml',
        'views/stock_picking_view.xml',
        # 'views/product_views.xml',

        # 'wizard/sale_coupon_apply_code_views.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
