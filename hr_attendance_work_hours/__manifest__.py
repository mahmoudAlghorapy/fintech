# -*- coding: utf-8 -*-
{
    'name': "SW - HR Attendance Work Hours",
    "summary": "HR_PKG_T2",
    "description": """
       HR_PKG_T2 
    """,
    'author': "Smart Way Business Solutions",
    'website': "https://www.smartway.co",
    'category': 'HR',
    'version': '1.0',
    'depends': ['base', 'hr_contract', 'hr_attendance', 'resource', 'hr_holidays'],
    'installable': True,
    'auto_install': False,
    'data': [
        'views/hr_attenadnce_views.xml',
    ],
    'license': "Other proprietary",
    'post_init_hook': 'post_init_hook',
}
