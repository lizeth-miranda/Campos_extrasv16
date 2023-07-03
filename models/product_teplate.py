# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class campos_extras(models.Model):
    _inherit = 'product.template'

    shape = fields.Char(
        string="Shape",
    )
    Dimensions = fields.Char(
        string="Dimensions",
    )
    Grade = fields.Char(
        string="Grade",
    )
    Length = fields.Char(
        string="Length",
    )
