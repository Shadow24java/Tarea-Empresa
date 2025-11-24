from odoo import models, fields

class Camion(models.Model):
    _name = 'paqueteria.camion'
    _description = 'Camión de transporte'

    matricula = fields.Char('Matrícula', required=True)

    empresa_id = fields.Many2one(
        'paqueteria.empresa',
        string='Empresa'
    )

    conductor_actual_id = fields.Many2one(
        'hr.employee',
        string='Conductor actual'
    )

    conductores_antiguos_ids = fields.Many2many(
        'hr.employee',
        string='Conductores anteriores'
    )

    fecha_itv = fields.Date('Última ITV')
    notas = fields.Text('Notas de mantenimiento')

    paquetes_ids = fields.One2many(
        'paqueteria.paquete',
        'camion_id',
        string='Paquetes transportados'
    )
