
{
    'name': 'Serial number in Sale Order,Purchase Order,Invoice',
    'version': '13.0.0.0',
    'author': "HAK Technologies",
    'summary': 'Serial number in Sale Order Linee',
    'description': """This module helps to show serial number in sale order lines.""",
    'category': 'Base',
    'website': 'https://www.haksolutions.com/',
    'license': 'AGPL-3',

    'depends': ['sale_management','account','purchase'],

    'data': [
        'views/sale_order_views.xml',
        'report/sale_order_report.xml',
    ],

    'qweb': [],
    'images': ['static/description/Banner.png'],

    'installable': True,
    'application': True,
    'auto_install': False,
}
