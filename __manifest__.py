# -*- coding: utf-8 -*-
{
    'name': "DGII Template Formats",
    'summary': """
    Este modulo sobre escribe el formato de las facturas para adaptarlo a la
    Norma General 06-2018 de la DGII.
    """,
    'description': """
        Adapta el formato de las facturas a la Norma General 06-2018 de la DGII.
    """,
    'author': "Yasmany Castillo",
    'website': "",
    'category': 'Localization',
    'version': '0.1',
    'depends': ['web', 'account', 'sale'],
    'data': [
        'report/report_invoice.xml',
        'report/report_sale.xml',
        'report/report_templates.xml',
    ],
}
