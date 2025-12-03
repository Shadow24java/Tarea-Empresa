# -*- coding: utf-8 -*-
# from odoo import http


# class NominasEmpleados(http.Controller):
#     @http.route('/nominas_empleados/nominas_empleados', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nominas_empleados/nominas_empleados/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nominas_empleados.listing', {
#             'root': '/nominas_empleados/nominas_empleados',
#             'objects': http.request.env['nominas_empleados.nominas_empleados'].search([]),
#         })

#     @http.route('/nominas_empleados/nominas_empleados/objects/<model("nominas_empleados.nominas_empleados"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nominas_empleados.object', {
#             'object': obj
#         })

