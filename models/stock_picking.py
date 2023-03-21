# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models


class campos_extras(models.Model):
    _inherit = 'stock.picking'

    numero_vale = fields.Char(
        string="Número de Vale",
    )
