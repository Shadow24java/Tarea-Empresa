{
    "name": "Guardería para empleados",
    "version": "18.0.1.0.0",
    "category": "Human Resources",
    "summary": "Servicio de guardería para empleados (delegación: empleado + evento)",
    "license": "LGPL-3",
    "depends": ["hr", "calendar"],
    "data": [
        "security/guarderia_security.xml",
        "security/ir.model.access.csv",
        "views/guarderia_views.xml",
        "views/guarderia_menus.xml",
    ],
    "installable": True,
    "application": True,
}
