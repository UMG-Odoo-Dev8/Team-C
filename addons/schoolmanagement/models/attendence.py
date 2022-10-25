from odoo import api,models,fields
class Attendence(models.Model):
    _name='attendence.model'
    _inherit=['mail.thread','mail.activity.mixin']
    _description='Student Attendence'
    section_name= fields.Many2one(comodel_name='subject.model', string='Section Name')
    date=fields.Date("Date")
    student_ids=fields.One2many('attendence_student.model','attendence_id',string='Student Name')
    class SchoolExam(models.Model):
      _name='attendence_student.model'
      _description='School_Attendence'
      student_id=fields.Many2one('school.model',string="Student Name:")
      roll_no=fields.Char("Roll No")
      attendence_id=fields.Many2one('attendence.model',string="Attendence ID")
      attendence = fields.Selection([
          ('presence','Presence'),
          ('leave','Leave'),
          ('absence','Absence')
      ], string='Attendence')
      @api.onchange('student_id')
      def onchange_student_id(self):
        self.roll_no=self.student_id.roll_no

    

    

     