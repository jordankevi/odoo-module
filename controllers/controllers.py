# -*- coding: utf-8 -*-
from odoo import http


class Test-module(http.Controller):
    @http.route('/test-module/', auth='public')
    def index(self, **kwargs):
        return "Bienvenue sur le module de test"

class Alpha-module(http.Controller):
	@http.route('test-module/alpha/objects', auth="public")
	def list(self, **kwargs):
		return http.request.render(
			'test-module.listing',
			{
				'root': '/test-module/alpha',
				'objects': http.request.env['test-module.alpha].search([]),
			}
		)
	
	@http.route('test-module/alpha/objects/<model("test-module.alpha"):obj>', auth='public')
	def object(self, obj, **kargs):
		return http.request.render('test-module.object', {'object', obj})

class beta-module(http.Controller):
	@http.route('test-module/beta/objects', auth="public")
	def list(self, **kwargs):
		return http.request.render(
			'test-module.listing',
			{
				'root': '/test-module/beta',
				'objects': http.request.env['test-module.beta].search([]),
			}
		)
	
	@http.route('test-module/beta/objects/<model("test-module.beta"):obj>', auth='public')
	def object(self, obj, **kargs):
		return http.request.render('test-module.object', {'object', obj})
