# -*- coding: utf-8 -*-
# from odoo import http


# class Supermodulo16(http.Controller):
#     @http.route('/supermodulo16/supermodulo16', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/supermodulo16/supermodulo16/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('supermodulo16.listing', {
#             'root': '/supermodulo16/supermodulo16',
#             'objects': http.request.env['supermodulo16.supermodulo16'].search([]),
#         })

#     @http.route('/supermodulo16/supermodulo16/objects/<model("supermodulo16.supermodulo16"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('supermodulo16.object', {
#             'object': obj
#         })
