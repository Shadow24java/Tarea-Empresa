# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class guarderia_servicio(models.Model):
#     _name = 'guarderia_servicio.guarderia_servicio'
#     _description = 'guarderia_servicio.guarderia_servicio'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

