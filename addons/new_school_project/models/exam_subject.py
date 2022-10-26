from odoo import api,models,fields
class SubjectExam(models.Model):
     _name='exam.model'
    
     _description='hello Exam'
     _rec_name="subject"
     
     subject=fields.Char("Subject")

     question_ids=fields.One2many('question.model','question_id',string='Exam Question')
     
    #  @api.onchange('subject')
    #  def onchange_subject(self):
    #     for rec in self:
    #         for line in self.question_ids:
    #             # print(".....",line)
    #             if rec.subject:
    #                 # print("Major:",line.major) #False
    #                 print("......",rec.subject)
    #                 line.major=rec.subject
    #             # else:
    #             #     line.major=rec.subject
class QuestionExam(models.Model):
      _name='question.model'
      _description='Exam_Question'
      _rec_name="question_id"

      
      question_id=fields.Many2one('exam.model',"Question ID")
      question=fields.Char("Question")
      
      answer = fields.Selection([
          ('true','True'),
          ('false','False')
      ])

      remark=fields.Char("Remark")
      qno=fields.Integer("No")
      active=fields.Boolean(string="Active",default=True)
      major=fields.Char()
      
      