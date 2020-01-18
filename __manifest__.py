# -*- coding: utf-8 -*-

{
    'name': 'course',
    'summary': """Manage courses""",
    'author': "Alejandro Sanchez",
    
    'category': 'Education',
    'version': '0.1',

    'depends': ['base'],

    'data': [
            'security/ir.model.access.csv',
            'views/course_view.xml',
            'views/task_view.xml',
        ],

    'application': True,
    'install': True,        
        
        
        
}
