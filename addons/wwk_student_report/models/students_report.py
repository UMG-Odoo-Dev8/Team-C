from odoo import fields,models

class SchoolSection(models.Model):
    _name = "school.section"
    _description = "This is section report"


class School(models.Model):
    _inherit = "school.project"
    _description = "This is students report"