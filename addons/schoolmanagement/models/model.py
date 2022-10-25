from odoo import models,fields
class School(models.Model):
     _name='school.model'
     _inherit=['mail.thread','mail.activity.mixin']
     _description='hello school'
     _rec_name="name"
     
     
     name=fields.Char("Name")
    
     role = fields.Selection([
          ('student','Student'),
          ('teacher','Teacher')
     ], string='Role')
     status = fields.Selection([
          ('old','Old'),
          ('new','New'),
          ('current','Current')
     ], string='Status')
     country = fields.Selection([
          ('myanmar','Myanmar'),
          ('thailand','Thailand'),
          ('America','American'),
          ('austrail','Austrail')
     ], string='Country')
     
     father_name=fields.Char("Father Name")
    
     roll_no=fields.Char("Roll No")
     degree=fields.Char("Degree")
     date_of_birth=fields.Date()
     ph_no=fields.Integer()
     gender=fields.Selection([
          ('male','Male'),
          ('female','Female'),
     ])
     age=fields.Integer("Age")
     address=fields.Char("Address")
     teacher_role=fields.Selection(selection=[
          ('principal','Principal'),
          ('teacher_head','Teacher Head'),
          ('teacher','Teacher')
     ])
     
     # active=fields.Boolean(string="Active",default=True)
    
     
     
     date_of_birth=fields.Date()
     avator=fields.Binary()
     description=fields.Text()
     priority=fields.Selection([
      ('0','Normal'),
      ('1','Low'),
      ('2','High'),
      ('3','Very High')],string="Priority")
     
