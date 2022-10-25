from odoo import api,models,fields
class SchoolAppointment(models.Model):
    _name='appointment.model'
    _inherit=['mail.thread','mail.activity.mixin']
    _description='school appointment'
    
   
    
    school_exam_line=fields.One2many('school.exam.line','exam_id',string='School Exam Line')
    subject_id = fields.Many2one(comodel_name='subject.model', string='Subject')
    teacher= fields.Char("Teacher")
    # def action_test(self):
    #     print("Button Clicked!!!")

    # def print_report(self):
    #     # print("kkk--->",self.reaf()[0])
    #     data = {
    #         'model':'appointment.model',
    #         'form' :self.read()[0]
    #     }
    #     print("Data",data)
    #     # return self.env.ref('schoolmanagement.report_').report_action(self,data=data)

#     priority widget
    priority=fields.Selection([
      ('0','Normal'),
      ('1','Low'),
      ('2','High'),
      ('3','Very High')],string="Priority")
    
    
#     On Change

    @api.onchange('subject_id')
    def onchange_subject_id(self):
      self.teacher=self.subject_id.teacher

class SchoolExam(models.Model):
    _name='school.exam.line'
    _description='School_Exam_Line'
    student_id=fields.Many2one('school.model',string="Student Name:")
    score=fields.Integer(string="Score:")
    exam_id=fields.Many2one('appointment.model',string="Exam ID")
    status=fields.Char(string="Status", readonly=True)
    @api.onchange('score')
    def OnchangeScore(self):
        if self.score >=0 and self.score <= 39:
            self.status = 'Fail'
        elif self.score >= 40 and self.score <= 79:
            self.status = 'Pass'
        elif self.score >= 80 and self.score <= 100:
            self.status = 'Pass with Distinations'
        else:
            self.status = 'Wrong Cridential'