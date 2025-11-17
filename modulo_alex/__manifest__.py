
{
    'name': 'Módulo Alex',
    'version': '0.3',
    'category': 'Ejemplo/ejemplo',
    'summary': 'Tarea 9 - Vistas personalizadas',
    'description': 'Módulo de ejemplo para Odoo que incluye un modelo de prueba con vistas personalizadas y control de acceso.',
    'author': 'Alex',
    'website': 'https://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/mi_modelo_prueba_views.xml',
        'views/menu.xml',
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

}

