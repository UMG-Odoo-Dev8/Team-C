from odoo import api,models,fields
class MonthlyReport(models.Model):
    _name='monthly.report'
    _inherit=['mail.thread','mail.activity.mixin']
    _description='Student Attendence'

    section_name=fields.Many2one("subject.model",string="Section Name:")
    monthly = fields.Selection([
        ('o1','Janauary'),
        ('02','Febuary'),
        ('03','March'),
        ('04','April'),
        ('05','May'),
        ('06','June'),
        ('07','July'),
        ('08','August'),
        ('09','September'),
        ('10','October'),
        ('11','November'),
        ('12','December')
    ],string="Month")
    attendence_line_ids=fields.One2many("school.monthly","attendence_line_id",string="Attendence Line Ids")

    def cal_percent(self,percent):
        return (percent/30)

    @api.onchange('section_name')
    def onchange_section_name(self):
        self.attendence_line_ids=[(5,0,0)]
        total_state={}
        roll_num = self.env['rollcall.line'].search([])
        roll_numbers = self.env['section.model'].search([])
        student_ids = self.env['school.model'].search([('role','=','student')])

        if student_ids:
    


            for student in student_ids:
                print("student Id", student.id,student.name)
                report_obj=roll_num.filtered(lambda x:int(x.student_id) == student.id and x.roll_call_id.date.strftime("%m") == self.monthly)
    
                print("Save....",roll_num.filtered(lambda x:int(x.student_id) == student.id and x.roll_call_id.date.strftime("%m") == self.monthly))
                filtered_student_line_ids = sum(roll_num.filtered(lambda x: x.student_id==student.id).mapped('state'))
                total_state.update({student.id:filtered_student_line_ids})
                print(filtered_student_line_ids)
                print("*"*100)
            print(total_state)

        if roll_numbers:
            for roll in roll_numbers:
                if self.section_name.section_name == roll.section_id.section_name:
                    vals = {
                        'roll_no':roll.roll_no,
                        'student_name':roll.student_id.name,
                        'total_present':total_state.get(int(roll.student_id)),
                        'rollcall_percent': self.cal_percent(total_state.get(int(roll.student_id)))
                    }
                    self.update({'attendence_line_ids':[(0,0,vals)]})

class SchoolMonthlyReport(models.Model):
    _name="school.monthly"
    _description="Monthly Report"

    roll_no=fields.Many2one("subject.model",string="Roll Number")
    student_name=fields.Many2one("subject.model",string="Student Name")
    total_present=fields.Integer("Total Present")
    rollcall_percent=fields.Float("Roll Call %")

    attendence_line_id=fields.Many2one("monthly.report",string="Attendence Line Model")

    
                    


