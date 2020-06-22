# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from datetime import datetime


class PlanProductionOrder(models.Model):
    _inherit = 'mrp.production'

    sale_id = fields.Char(
        compute='_compute_sale_id',
        store=True,    
    )

    @api.depends('origin')
    def _compute_sale_id (self):
