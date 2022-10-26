from importlib.metadata import files
from odoo import fields,models,api

class SchoolRollCall(models.Model):
    _name = "school.rollcall"
    _description = "School Roll Call"

    sec_name = fields.Many2one('school.section', string="Section Name:")
    date = fields.Date("Date:")
    teacher_head = fields.Char("Teacher Head")
    
    line_ids = fields.One2many('rollcall.line','roll_call_id',string= "Roll Call Line")

    
    @api.onchange('sec_name')
    def _onchange_sec_name(self):
        self.teacher_head = self.sec_name.teacher_head.name

    @api.onchange('sec_name')
    def onchange_sec_name(self):
        self.line_ids=[(5,0,0)]
        roll_num = self.env['school.section.line'].search([])
        if roll_num:
            for roll in roll_num:
                if self.sec_name.name == roll.section_id.name:
                    vals = {
                        'student_id':int(roll.student_name),
                        'roll_no':roll.roll_no,
                        'student_name':roll.student_name.name
                    }
                    self.update({'line_ids':[(0,0,vals)]})

    

class SchoolRollCallLine(models.Model):
    _name = "rollcall.line"
    _description = "Roll Call Line"

    student_id=fields.Char("Student_ID")
    roll_no = fields.Char("Roll Number")
    student_name = fields.Char("Student Name")
    morning = fields.Boolean('Morning')
    afternoon = fields.Boolean('Afternoon')
    leave = fields.Boolean('Leave')

    state = fields.Float(string="State",compute="_compute_present",store=True)

    roll_call_id = fields.Many2one('school.rollcall',string="Roll Call ID")

    @api.depends('morning', 'afternoon','leave')
    def _compute_present(self):
        for attendance in self:
            if not attendance.morning and not attendance.afternoon and not attendance.leave:
                attendance.state = 0
            elif not attendance.morning and not attendance.afternoon and attendance.leave:
                attendance.state=1
            elif attendance.morning and attendance.afternoon:
                attendance.state = 1
            elif (attendance.morning or attendance.afternoon) and not attendance.leave:
                attendance.state = 0.5
            elif (attendance.morning or attendance.afternoon) and attendance.leave:
                attendance.state = 1
            else:
                return False

    
