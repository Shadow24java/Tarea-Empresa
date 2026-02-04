# -*- coding: utf-8 -*-
# from odoo import http


# class /var/lib/odoo/addons/18.0/servicioGuarderia(http.Controller):
#     @http.route('//var/lib/odoo/addons/18.0/servicio_guarderia//var/lib/odoo/addons/18.0/servicio_guarderia', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//var/lib/odoo/addons/18.0/servicio_guarderia//var/lib/odoo/addons/18.0/servicio_guarderia/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/var/lib/odoo/addons/18.0/servicio_guarderia.listing', {
#             'root': '//var/lib/odoo/addons/18.0/servicio_guarderia//var/lib/odoo/addons/18.0/servicio_guarderia',
#             'objects': http.request.env['/var/lib/odoo/addons/18.0/servicio_guarderia./var/lib/odoo/addons/18.0/servicio_guarderia'].search([]),
#         })

#     @http.route('//var/lib/odoo/addons/18.0/servicio_guarderia//var/lib/odoo/addons/18.0/servicio_guarderia/objects/<model("/var/lib/odoo/addons/18.0/servicio_guarderia./var/lib/odoo/addons/18.0/servicio_guarderia"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/var/lib/odoo/addons/18.0/servicio_guarderia.object', {
#             'object': obj
#         })

