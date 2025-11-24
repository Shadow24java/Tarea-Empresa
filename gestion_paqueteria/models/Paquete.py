from odoo import models, fields

class Paquete(models.Model):
    _name = 'paqueteria.paquete'
    _description = 'Paquete transportado'

    name = fields.Char('N.º Seguimiento', required=True)
    remitente_id = fields.Many2one('res.partner', string='Remitente')
    destinatario_id = fields.Many2one('res.partner', string='Destinatario')

    country = fields.Char('País')
    region = fields.Char('Región')
    municipio = fields.Char('Municipio')
    calle = fields.Char('Calle')
    numero = fields.Char('Número')
    datos_extra = fields.Char('Datos adicionales')

    camion_id = fields.Many2one('paqueteria.camion', string='Camión')
    
    actualizaciones_ids = fields.One2many(
        'paqueteria.seguimiento',
        'paquete_id',
        string='Actualizaciones'
    )
