# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class mi_modulo_prueba(models.Model):
#     _name = 'mi_modulo_prueba.mi_modulo_prueba'
#     _description = 'mi_modulo_prueba.mi_modulo_prueba'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

