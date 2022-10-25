from odoo import api,models,fields
class Attendence(models.Model):
    _name='attendence.record'
    _inherit=['mail.thread','mail.activity.mixin']
    _description='Student Attendence'
    sec_name = fields.Many2one('subject.model', string='Section Name')
    date=fields.Date("Date:")
    teacher_id= fields.Char('Teacher Head')
    roll_call_ids = fields.One2many('rollcall.line', 'roll_call_id', string='Roll Call Line')

    @api.onchange('sec_name')
    def _onchange_sec_name(self):
        self.teacher_id = self.sec_name.teacher_id.name

    @api.onchange('sec_name')
    def onchange_sec_name(self):
        self.roll_call_ids=[(5,0,0)]
        roll_num = self.env['section.model'].search([])
        if roll_num:
            for roll in roll_num:
                if self.sec_name.section_name == roll.section_id.section_name:
                    vals = {
                        'roll_no':roll.roll_no,
                        'student_id':int(roll.student_id),
                        'student_name':roll.student_id.name
                    }
                    self.update({'roll_call_ids':[(0,0,vals)]})

class SchoolRollCall(models.Model):
    _name='rollcall.line'
    _description='Roll Call Line'

    roll_no=fields.Char("Roll Number")
    student_id=fields.Char()
    student_name=fields.Char("Student Name")
    morning=fields.Boolean("Morning")
    afternoon=fields.Boolean("Afternoon")
    leave=fields.Boolean("Leave")
    state=fields.Float(string="State",compute='_compute_present', store=True)

    roll_call_id=fields.Many2one("attendence.record",string="Roll Call Id")


    # @api.depends('morning', 'afternoon')
    # def _compute_present(self):
    #     for attendance in self:
    #         if not attendance.morning and not attendance.afternoon:
    #             attendance.state = 0
    #         elif attendance.morning and attendance.afternoon:
    #             attendance.state=1
    #         elif attendance.morning or attendance.afternoon:
    #             attendance.state = 0.5
    #         else:
    #             return False
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