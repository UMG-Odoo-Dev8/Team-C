from odoo import api,models,fields
class School(models.TransientModel):
     _name='exam.student.record'
     _inherit=['mail.thread','mail.activity.mixin']
     _description='Exam Student Record'

     student_id= fields.Many2one('school.exam.line', string="Name")

     def action_record(self):
        print("Button Clicked!!!")

     def cancel(self):
        print("Button Click")