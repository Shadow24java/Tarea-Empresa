# -*- coding: utf-8 -*-
# from odoo import http


# class GuarderiaServicio(http.Controller):
#     @http.route('/guarderia_servicio/guarderia_servicio', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/guarderia_servicio/guarderia_servicio/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('guarderia_servicio.listing', {
#             'root': '/guarderia_servicio/guarderia_servicio',
#             'objects': http.request.env['guarderia_servicio.guarderia_servicio'].search([]),
#         })

#     @http.route('/guarderia_servicio/guarderia_servicio/objects/<model("guarderia_servicio.guarderia_servicio"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('guarderia_servicio.object', {
#             'object': obj
#         })

