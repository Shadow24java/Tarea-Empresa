{
    'name': 'Gestión de Paquetería',
    'version': '1.0',
    'author': 'Alejandro',
    'category': 'Logistica',
    'summary': 'Gestión de camiones, paquetes y seguimiento',
    'depends': ['base', 'hr'],
    'data': [
        'security/models.xml',
        'security/ir.model.access.csv',
        'views/Paquete_views.xml',
        'views/Seguimiento_views.xml',
        'views/Camion_views.xml',
        'views/empresa_views.xml',
        'views/Menu.xml',
        'views/templates.xml',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

