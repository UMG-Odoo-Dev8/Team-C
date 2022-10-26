
from datetime import date, timedelta,datetime
from email.policy import default
from time import strftime
from time import strptime

from odoo import fields,models,api

class SchoolAttendance(models.Model):
    _name = "school.attendance"
    _description = "School Attendance"

    section_name = fields.Many2one('school.section', string="Section Name:")
    monthly = fields.Selection([
        ('01','Janauary'),
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

    attendance_line_ids = fields.One2many("school.attendance.line","attendance_line_id",string="Attendance Report")

    def check_percent(self,parm_percent):
        per=""
        if parm_percent < 0.75:
            per="Rejected"
        else:
            per="Accessed"
        return per
    
    def attendance_days(self,from_date,to_date):
        dates = (from_date + timedelta(idx)
         for idx in range((to_date - from_date).days+1))
        res = sum(1 for day in dates if day.weekday() < 5)
        print("Total business days in range : " + str(res))

        return res

    def cal_percent(self,param_point):
        # print(param_point)
        percent=0.0
        # if param_point!=0.0:
        if self.monthly in ['April','June','September','November']:
            days=self.attendance_days(datetime.strptime(str(date.today().year)+"-"+self.monthly+ "-01","%Y-%m-%d"),datetime.strptime(str(date.today().year)+"-"+self.monthly+ "-30","%Y-%m-%d"))           
            percent=((30-days)+param_point)/30
        elif self.monthly=='February':
            days=self.attendance_days(datetime.strptime(str(date.today().year)+"-"+self.monthly+ "-01","%Y-%m-%d"),datetime.strptime(str(date.today().year)+"-"+self.monthly+ "-28","%Y-%m-%d"))           
            percent=((28-days)+param_point)/28
        else:
            # print(datetime.strptime(str(date.today().year)+"-"+self.months+ "-01","%Y-%B-%d"),datetime.strptime(str(date.today().year)+"-"+self.months+ "-31","%Y-%B-%d"))
            days=self.attendance_days(datetime.strptime(str(date.today().year)+"-"+self.monthly+ "-01","%Y-%m-%d"),datetime.strptime(str(date.today().year)+"-"+self.monthly+ "-31","%Y-%m-%d"))           
            percent=((31-days)+param_point)/31
        return percent

    @api.onchange('section_name','monthly')
    def onchange_section_name(self):
        if self.section_name and self.monthly:
            self.attendance_line_ids=[(5,0,0)]
            total_state={}

            roll_num = self.env['rollcall.line'].search([])
            roll_numbers = self.env['school.section.line'].search([])
            student_ids = self.env['school.project'].search([('role','=','student')])

            if student_ids:
                for student in student_ids:
                    filtered_student_line_ids = sum(roll_num.filtered(lambda x:int(x.student_id) == student.id and x.roll_call_id.date.strftime("%m") == self.monthly).mapped("state"))

                    total_state.update({student.id:filtered_student_line_ids})
                    
                    print(filtered_student_line_ids)
                    print("*"*100)
            print(total_state)

            if roll_numbers:
                for roll in roll_numbers:
                    tot_state = 0.0
                    percent=0
                    if self.section_name.name == roll.section_id.name:
                        tot_state = total_state.get(int(roll.student_name))
                        percent = self.cal_percent(tot_state)
                        vals = {
                            
                            'roll_no':roll.roll_no,
                            'student_name':roll.student_name.name,
                            'total_attendance':tot_state,
                            'rollcall_percent': percent ,# get percentage same with student id (
                            'permit':self.check_percent(percent)
                        }
                        self.update({'attendance_line_ids':[(0,0,vals)]})

            
            
           

   
    

class SchoolAttendanceLine(models.Model):
    _name = "school.attendance.line"
    _description = "School Attendance Line"
    _rec_name="roll_no"

    roll_no = fields.Char("Roll Number")
    student_name = fields.Char("Student Name")
    total_attendance = fields.Float("Total Attendance")
    
    rollcall_percent = fields.Float("RollCall %")
    permit = fields.Char(string="Permit")
    
    attendance_line_id = fields.Many2one("school.attendance",string="Attendance Line ID")


class SchoolLeave(models.Model):
    _name = "school.leave"
    _description = "School Leave" 

    