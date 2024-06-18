# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models



class acuerdo_compra(models.Model):
    _inherit = 'purchase.requisition'

    state = fields.Selection(selection_add=[('almacen', 'Almacen'),('done',)], ondelete={'almacen': 'set default'})
    state_blanket_order = fields.Selection(selection_add=[('almacen', 'Almacen'),('done',)])
    
    def action_almacen(self):
        print("button clicked!!!")
        for rec in self:
            rec.state = 'almacen'
