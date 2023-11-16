# -*- coding: utf-8 -*-
# from odoo import http


# class NewHeaderSnippet(http.Controller):
#     @http.route('/new_header_snippet/new_header_snippet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_header_snippet/new_header_snippet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_header_snippet.listing', {
#             'root': '/new_header_snippet/new_header_snippet',
#             'objects': http.request.env['new_header_snippet.new_header_snippet'].search([]),
#         })

#     @http.route('/new_header_snippet/new_header_snippet/objects/<model("new_header_snippet.new_header_snippet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_header_snippet.object', {
#             'object': obj
#         })
