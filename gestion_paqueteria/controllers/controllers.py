# -*- coding: utf-8 -*-
# from odoo import http


# class GestionPaqueteria(http.Controller):
#     @http.route('/gestion_paqueteria/gestion_paqueteria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_paqueteria/gestion_paqueteria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_paqueteria.listing', {
#             'root': '/gestion_paqueteria/gestion_paqueteria',
#             'objects': http.request.env['gestion_paqueteria.gestion_paqueteria'].search([]),
#         })

#     @http.route('/gestion_paqueteria/gestion_paqueteria/objects/<model("gestion_paqueteria.gestion_paqueteria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_paqueteria.object', {
#             'object': obj
#         })

