from datetime import datetime
from odoo import api,models,fields
import math
class SubjectExam(models.Model):
     _name='examination.model'
    
     _description='hello Examination'
     
    
     roll_no=fields.Many2one('school.section.line',string="Roll No")
     name = fields.Char("Student Name")
     section_name=fields.Many2one("school.section","Section")
     subject= fields.Many2one('exam.model', string='Subject')
     exam_date=fields.Datetime("Exam DateTime")
     question_ids=fields.One2many('equestion.model','question_id',string='Exam Question')
     default_value=fields.Char("Marks")
     status=fields.Char("Status")
      
     @api.onchange('roll_no')
     def onchange_roll_no(self):
        self.name=self.roll_no.student_name.name
     
     @api.onchange('subject')
     def onchange_subject(self):
        # global answer_list
        # answer_list=[]
        self.question_ids=[(5,0,0)]
        questions = self.env['question.model'].search([])
        print(questions)
        if questions:
            for ques in questions:
                
                if self.subject.subject == ques.question_id.subject:
                    vals = {
                        'question':ques.question,
                        'answer':ques.answer
                          
                    }
                    self.update({'question_ids':[(0,0,vals)]})

     def submit_result(self):
        print("*"*100)
        mark =0
        question_count=0
        print(self.question_ids)
        for question_id in self.question_ids:
            question_count +=1
            # print(question_id)
            if question_id.answer == question_id.answer_choice:
                print(question_id.question)
                mark +=1
        self.default_value = mark
        if(mark>=math.ceil(question_count/2)):
            self.status='Pass'
        else:
            self.status='Fail'
        # mark=0
        # print('/////////////////////////', mark)
        # print('//////////////////', self.default_value)
       # iterate=0
        # answers = self.env['equestion.model'].search([])
        # if answers:
            # for ans in answers:
                # print(".....Choice ",ans.answer)
                # if self.subject.subject==ans.question_id.subject:
                # if ans.answer_choice==ans.answer:
                    # mark +=1  
                # print("mark",mark)             
                # self.default_value=str(mark)
                
     class QuestionExam(models.Model):
      _name='equestion.model'
      _description='Exam_Question'
      question=fields.Char("Question")
      
      question_id=fields.Many2one("examination.model","Question ID")
      answer_choice=fields.Selection(selection=[
        ('true','True'),
        ('false','False'),
      ])
      answer=fields.Selection(selection=[
          ('true','True'),
          ('false','False'),
      ])
      remark=fields.Integer("Remark")
      

     
                    

        

       
      

      


      
      
