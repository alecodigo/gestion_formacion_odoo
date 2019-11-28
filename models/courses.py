# -*- coding: utf-8 -*-

from odoo import models, fields, api, _ 



class Careers(models.Model):
    _name = 'careers'

    name = fields.Char(string='Career')
    progress = fields.Float(string='Progress')
    courses_ids = fields.One2many('courses', 'careers_id', string='Courses')
    description = fields.Text(string='Description')
    date_start = fields.Date(string='Date start')
    date_end = fields.Date(string='Date end')
    projects_ids = fields.One2many('projects' ,'career_id', string='Projects')

class Courses(models.Model):
    _name = 'courses'

    name = fields.Char(string='Course')
    progress = fields.Float(string='Progress')
    date_start = fields.Date(string='Date start')
    date_end = fields.Date(string='Date end')
    careers_id = fields.Many2one('careers', string='Career')
    topics_ids = fields.One2many('course.topics', 'course_id', string='Topics')

class CourseTopics(models.Model):
    _name = 'course.topics'

    name = fields.Char(string='Topic')
    status = fields.Selection([ 
                                ('done','Done'),
                                ('in_progress','In progress'),
                                ('to_do','To-do'),
                            ],string='status')
    course_id = fields.Many2one('courses', string='Courses')


class Projects(models.Model):
    _name = 'projects'


    name = fields.Char(string='Project')
    carrer_id = fields.Many2one('careers', string='career')
    description = fields.Text(string='description')
    tech_ids = fields.One2many('technology' ,'project_id', string='Technologies')
    career_id = fields.Many2one('careers', string='Career')

class Technology(models.Model):
    _name = "technology"


    name = fields.Char(string='Name')
    project_id = fields.Many2one(string='Projects')
