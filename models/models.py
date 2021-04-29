# -*- coding: utf-8 -*-

from odoo import fields, models
# from odoo import api


class Alpha(models.Model):
	_name = "test-module.alpha"
	
	name = fields.Char(required=true)
	date = fields.Date(string="Starting date")
	address = fields.Char()
	key = fields.Char()
	betas = fields.One2Many(
		'test-module.beta',
		'alpha_id',
		ondelete='set null'
	)
	
	
class Beta(models.Model):
	_name = "test-module.beta"
	
	name = fields.Char(string="Name", required=true)
	phone = fields.Char(string="Phone number")
	price = fields.Integer(string="Price")

# class test-module(models.Model):
#     _name = 'test-module.test-module'
#     _description = 'test-module.test-module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
