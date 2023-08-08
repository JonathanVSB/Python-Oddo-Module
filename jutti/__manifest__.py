# -*- coding: utf-8 -*-
{
    'name': "Jutti",

    'summary': """
        Exemple de mòdul incomplert per gestionar un modul propi""",

    'description': """
        Aprendre a un mòdul a Odoo
    """,

    'author': "Jonathan Segura",
    'website': "https://campus.proven.cat/course/view.php?id=268",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    #Desactivem la gestió d'usuaris i a nivell gràfic treballarem com a súperusuari
    'data': [
        #'security/ir.model.access.csv',
	'views/jutti_view.xml',
    ],
    # only loaded in demonstration mode
    #'demo': ['demo/demo.xml',],
    'installable': True,
    'application': True,
    'autoinstall': False,
}
