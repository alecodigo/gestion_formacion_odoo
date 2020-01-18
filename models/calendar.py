# -*- coding: utf-8 -*-


from odoo import _, api, fields, models



class task(models.Model):
    _name = 'task'
    _description = 'Task of day'

    name = fields.Many2one('courses', string='Course')
    state = fields.Selection([('draft','Draft'),
                               ('done','Done')], string='State')
    date_start = fields.Date(string='Date start')
    date_end = fields.Date(string='Date end')

