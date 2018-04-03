# -*- coding: utf-8 -*-
{
    'name': "Daily sales report",
    'summary': "Send daily sales report on mail",
    'author': "Karthi D<karthidev1606@gmail.com>",
    'license': "AGPL-3",
    'category': 'Sales',
    'version': '10.0.0.0.1',
    'depends': [
        'base',
        'mail',
        'sale',
    ],
    'data': [
        'data/daily_sale_report_data.xml',
    ],
}