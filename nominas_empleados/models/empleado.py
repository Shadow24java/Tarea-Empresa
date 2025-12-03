from odoo import models, fields

class Empleado(models.Model):
    _name = "nomina.empleado"
    _description = "Empleado"

    name = fields.Char(string="Nombre", required=True)
    dni = fields.Char(string="DNI")
    email = fields.Char(string="Email")
    telefono = fields.Char(string="Teléfono")

    nomina_ids = fields.One2many(
        comodel_name="nomina.nomina",
        inverse_name="empleado_id",
        string="Nóminas"
    )

    declaracion_ids = fields.One2many(
        comodel_name="nomina.declaracion.renta",
        inverse_name="empleado_id",
        string="Declaraciones de Renta"
    )
