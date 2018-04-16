# -*- coding: utf-8 -*-
{
    'name': "Sale blocked orders",
    'summary': "Menu for blocked orders",
    'author': "Karthi D<karthidev1606@gmail.com>",
    'license': "AGPL-3",
    'category': 'Sales',
    'version': '10.0.0.0.1',
    'depends': [
        'base',
        'sale',
        'sale_order_blockages',
    ],
    'data': [
        'views/sale_blocked_orders_views.xml',
    ],
}
