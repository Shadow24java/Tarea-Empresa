from odoo import models, fields
from datetime import date

class PaqueteriaSeguimiento(models.Model):
    _name = "paqueteria.seguimiento"
    _description = "Seguimiento del paquete"

    fecha = fields.Date(
        string="Fecha",
        default=lambda self: date.today()
    )
    estado = fields.Selection(
        [
            ('recibido', 'Recibido en almacén'),
            ('en_ruta', 'En ruta'),
            ('entregado', 'Entregado'),
            ('incidencia', 'Incidencia'),
        ],
        string="Estado",
        required=True
    )
    notas = fields.Text(string="Notas adicionales")

    paquete_id = fields.Many2one(
        "paqueteria.paquete",
        string="Paquete",
        required=True,
        ondelete='cascade'
    )
