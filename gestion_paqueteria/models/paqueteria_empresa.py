from odoo import models, fields

class PaqueteriaEmpresa(models.Model):
    _name = "paqueteria.empresa"
    _description = "Empresa de Paquetería"

    name = fields.Char("Nombre", required=True)
    telefono = fields.Char("Teléfono")
    direccion = fields.Char("Dirección")

    camion_ids = fields.One2many(
        "paqueteria.camion",
        "empresa_id",
        string="Camiones"
    )
