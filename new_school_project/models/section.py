from odoo import fields,models,api

class SchoolSection(models.Model):
    _name = "school.section"
    _description = "School Section"
    # _rec_name = "name"
    
    # section_name = fields.Selection([('section_a','Section-A'),('section_b','Section-B'),('section_c','Section-C')],string = "Section Name:")
    name = fields.Char("Section Name")
    teacher_head = fields.Many2one("school.project",string="Teacher Head:",domain="[('teacher_role','=','teacher_head')]")

    section_line =fields.One2many('school.section.line', 'section_id', string='School Section Line')

    # @api.onchange('name')
    # def _onchange_name(self):
    #     for rec in self:
    #         for line in self.section_line:
    #             if rec.name:
    #                 print("....", rec.name)
    #                 line.section_name = rec.name

class SchoolSectionLine(models.Model):
    _name='school.section.line'
    _description = 'Section Line'
    _rec_name = "roll_no"

    student_name = fields.Many2one("school.project",string="Student Name",domain="[('role','=','student')]") 
    roll_no = fields.Char ("Roll Number")
    
    section_id = fields.Many2one('school.section',string="Section ID:")

    
    


