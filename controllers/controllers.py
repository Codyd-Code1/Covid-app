# -*- coding: utf-8 -*-
# from odoo import http


# class Covid-app(http.Controller):
#     @http.route('/covid-app/covid-app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/covid-app/covid-app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('covid-app.listing', {
#             'root': '/covid-app/covid-app',
#             'objects': http.request.env['covid-app.covid-app'].search([]),
#         })

#     @http.route('/covid-app/covid-app/objects/<model("covid-app.covid-app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('covid-app.object', {
#             'object': obj
#         })
