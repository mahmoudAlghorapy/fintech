# -*- coding: utf-8 -*-
{
    'name': "Product Enhancement",
    'category': 'Product',
    'version': '17.0',
    'depends': ['product', 'base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/brand.xml',
        'views/model.xml',
        'views/product_views.xml',

        # 'wizard/sale_coupon_apply_code_views.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
