# -*- coding: utf-8 -*-
{
    'name': "escuela",

    'summary': "Módulo para la gestión de una escuela",

    'description': """
Módulo para gestionar estudiantes, asignaturas y grupos en una escuela.
Permite la creación y administración de estos modelos mediante vistas personalizadas.
    """,

    'author': "deme3c",
    'website': "https://github.com/deme3c",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',  # Archivo de permisos
        'views/estudiante_vista.xml',    # Vista de estudiantes
        'views/asignatura_vista.xml',    # Vista de asignaturas
        'views/grupo_vista.xml',         # Vista de grupos
        'views/escuela_menu.xml',        # Menús y acciones
        'reports/report_grupos.xml',     # Generar reportes
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

