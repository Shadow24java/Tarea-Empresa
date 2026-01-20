# -*- coding: utf-8 -*-
# from odoo import http


# class HrEmployeeDniNss(http.Controller):
#     @http.route('/hr_employee_dni_nss/hr_employee_dni_nss', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_employee_dni_nss/hr_employee_dni_nss/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_employee_dni_nss.listing', {
#             'root': '/hr_employee_dni_nss/hr_employee_dni_nss',
#             'objects': http.request.env['hr_employee_dni_nss.hr_employee_dni_nss'].search([]),
#         })

#     @http.route('/hr_employee_dni_nss/hr_employee_dni_nss/objects/<model("hr_employee_dni_nss.hr_employee_dni_nss"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_employee_dni_nss.object', {
#             'object': obj
#         })

