# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloAlex(http.Controller):
#     @http.route('/modulo_alex/modulo_alex', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_alex/modulo_alex/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_alex.listing', {
#             'root': '/modulo_alex/modulo_alex',
#             'objects': http.request.env['modulo_alex.modulo_alex'].search([]),
#         })

#     @http.route('/modulo_alex/modulo_alex/objects/<model("modulo_alex.modulo_alex"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_alex.object', {
#             'object': obj
#         })

