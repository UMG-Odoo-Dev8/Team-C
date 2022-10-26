from email.policy import default
from odoo import fields,models

class School(models.Model):
    _name = "school.project"
    _description = "School Project"
    _rec_name = "name"
    
    
    avatar = fields.Binary("Profile Photo")
    # roll_no = fields.Char("Roll Number:")
    name = fields.Char("Name:",required=True)
    dob = fields.Date("Date Of Birth:")
    father_name = fields.Char("Father Name:")
    ph_no = fields.Char("Phone Number:")
    address = fields.Text("Address:")
    gender = fields.Selection([('male','Male'),('female','Female')])
    role = fields.Selection([('student','Student'),('teacher','Teacher')],string='Role:',default="student")
    teacher_role = fields.Selection([('principal','Principal'),('teacher_head','Teacher Head'),('teacher','Subject Teacher')],string='Teacher Role:',default="teacher")
    
    
    



