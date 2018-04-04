# -*- coding: utf-8 -*-
{
    'name': "Weekly sales report",
    'summary': "Send weekly sales report on mail",
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
        'data/weekly_sales_report_data.xml',
    ],
}