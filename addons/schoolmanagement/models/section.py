from odoo import api,models,fields
class SchoolAppointment(models.Model):
    _name='subject.model'
    _inherit=['mail.thread','mail.activity.mixin']
    _description='school subject'
    _rec_name='section_name'
    
    section_name=fields.Char("Section Name")
    teacher_id = fields.Many2one(comodel_name='school.model', string='Teacher Head')
    teacher=fields.Many2many("school.model",string='Teacher')
    student_ids=fields.One2many('section.model','section_id',string='Student Name')
    









    # _rec_name='subject'
    # subject=fields.Char("Subject")
    # teacher = fields.Char("Teacher")
    # active=fields.Boolean(string="Active",default=True)
    priority=fields.Selection([
      ('0','Normal'),
      ('1','Low'),
      ('2','High'),
      ('3','Very High')],string="Priority") 
    class SchoolExam(models.Model):
      _name='section.model'
      _description='School_Section'
      _rec_name="roll_no"
      
      student_id=fields.Many2one('school.model',string="Student Name:")
      roll_no=fields.Char("Roll No")
      
      section_id=fields.Many2one('subject.model',string="Section ID")
      @api.onchange('student_id')
      def onchange_student_id(self):
        self.roll_no=self.student_id.roll_no


      
     
    
    # student_id = fields.Many2one(comodel_name='school.model', string='Student')
#  field_name_id = fields.Many2one('comodel_name', string='field_name') 