# -*- coding: utf-8 -*-
# from odoo import http


# class MiModuloDefinitivo(http.Controller):
#     @http.route('/mi_modulo_definitivo/mi_modulo_definitivo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mi_modulo_definitivo/mi_modulo_definitivo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mi_modulo_definitivo.listing', {
#             'root': '/mi_modulo_definitivo/mi_modulo_definitivo',
#             'objects': http.request.env['mi_modulo_definitivo.mi_modulo_definitivo'].search([]),
#         })

#     @http.route('/mi_modulo_definitivo/mi_modulo_definitivo/objects/<model("mi_modulo_definitivo.mi_modulo_definitivo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mi_modulo_definitivo.object', {
#             'object': obj
#         })

