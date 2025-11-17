# -*- coding: utf-8 -*-
# from odoo import http


# class MiModuloPrueba(http.Controller):
#     @http.route('/mi_modulo_prueba/mi_modulo_prueba', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mi_modulo_prueba/mi_modulo_prueba/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mi_modulo_prueba.listing', {
#             'root': '/mi_modulo_prueba/mi_modulo_prueba',
#             'objects': http.request.env['mi_modulo_prueba.mi_modulo_prueba'].search([]),
#         })

#     @http.route('/mi_modulo_prueba/mi_modulo_prueba/objects/<model("mi_modulo_prueba.mi_modulo_prueba"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mi_modulo_prueba.object', {
#             'object': obj
#         })

