# -*- coding: utf-8 -*-

import logging
from datetime import datetime, timedelta, date

from odoo import models, fields, api, _ 


_logger = logging.getLogger(__name__)


class Careers(models.Model):
    _name = 'careers'

    name = fields.Char(string='Career')
    state = fields.Selection([('important', 'Important'),
                               ('no_important', 'Not important'),
                               ('urgent', 'Urgent'),
                               ('done', 'Done'),], string='Status')
    progress = fields.Float(string='Progress')
    courses_ids = fields.One2many('courses', 'careers_id', string='Courses')
    description = fields.Text(string='Description')
    date_start = fields.Date(string='Date start')
    date_end = fields.Date(string='Date end')
    projects_ids = fields.One2many('projects' ,'career_id', string='Projects')  

    
    def important(self):
        self.state = 'important'


    def not_important(self):
        self.state = 'no_important'


    def urgent(self):
        self.state = 'urgent'


    def done(self):
        self.state = 'done'


class Courses(models.Model):
    _name = 'courses'


    #@api.multi
    #@api.depends('progress')
    def _progress(self):
        pass
        #total_courses = 0
        #for courses in self.topics_ids:
        #for topic in courses:
        #if topic.state == 'done':
        #total_courses += 1
        #r = 100 / total_courses
        #self.progress = self.progress + r



    name = fields.Char(string='Course')
    state = fields.Selection([
                                ('done', 'Done'),
                                ('in_progress', 'In progress'),
                                ('to_do', 'To do'),
                             ], string='Status', default='to_do')
    progress = fields.Float(compute='_progress', string='Progress')
    date_start = fields.Date(string='Date start')
    date_end = fields.Date(string='Date end')
    careers_id = fields.Many2one('careers', string='Career')
    topics_ids = fields.One2many('course.topics', 'course_id', string='Topics')


    def to_do(self):
        self.state = 'to_do'
        

    def done(self):
        self.state = 'done'


    def in_progress(self):
        self.state = 'in_progress'


class CourseTopics(models.Model):
    _name = 'course.topics'

    name = fields.Char(string='Topic')
    state = fields.Selection([  
                                ('to_do','To-do'),
                                ('in_progress','In progress'),
                                ('done','Done'),
                            ],string='Status', default='to_do')
    course_id = fields.Many2one('courses', string='Courses')
    date_start = fields.Date(string='Date start')
    date_end = fields.Date(string='Date end')
    observation = fields.Text(string='Observation')


    def to_do(self):
        self.state = 'to_do'


    def done(self):
        self.state = 'done'
        self.date_end = fields.Date.to_string(datetime.now())
    

    def in_progress(self):
        self.state = 'in_progress'


class Projects(models.Model):
    _name = 'projects'


    name = fields.Char(string='Project')
    state = fields.Selection([('done', 'Done'),
                              ('to_do', 'To do')], 
                              string='Status', default='to_do')
    carrer_id = fields.Many2one('careers', string='Carrer')
    description = fields.Text(string='description')
    tech_ids = fields.One2many('technology' ,'project_id', string='Technologies')
    career_id = fields.Many2one('careers', string='Career')
    note = fields.Text(string='Note')
    

    def done(self):
        self.state = 'done'


class Technology(models.Model):
    _name = "technology"


    name = fields.Char(string='Name')
    project_id = fields.Many2one(string='Projects')
    level_skill = fields.Selection([('very_low', 'Very low'),
                                    ('low', 'Low'),
                                    ('medium', 'Medium'),
                                    ('high', 'High'),
                                    ('very_high', 'Very high')], string='Skill level')
