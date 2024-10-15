# -*- coding: utf-8 -*-
# from odoo import http


# class Supermodulo17(http.Controller):
#     @http.route('/supermodulo17/supermodulo17', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/supermodulo17/supermodulo17/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('supermodulo17.listing', {
#             'root': '/supermodulo17/supermodulo17',
#             'objects': http.request.env['supermodulo17.supermodulo17'].search([]),
#         })

#     @http.route('/supermodulo17/supermodulo17/objects/<model("supermodulo17.supermodulo17"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('supermodulo17.object', {
#             'object': obj
#         })

