from odoo import models, fields

class ModeloPrueba(models.Model):
    _name = "modulo_alex_prueba"
    _description = 'Modelo de Prueba para el Módulo Alex'

    name = fields.Char(string="Nombre")
    descripcion = fields.Text(string="Descripción")
    fecha = fields.Date(string="Fecha de creación")
    ex_field = fields.Char(string="Example")
    ex_field_2 = fields.Char(string="Example")
    ex_field_3 = fields.Char(string="Example")