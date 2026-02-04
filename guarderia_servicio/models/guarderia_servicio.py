# -*- coding: utf-8 -*-
from odoo import fields, models

class GuarderiaServicio(models.Model):
    _name = "guarderia.servicio"
    _description = "Servicio de guardería"

    
    _inherits = {
        "hr.employee": "monitor_id",
        "calendar.event": "event_id",
    }

    
    monitor_id = fields.Many2one(
        "hr.employee",
        string="Monitor/a (Empleado)",
        required=True,
        ondelete="cascade",
        index=True,
        auto_join=True,
    )
    event_id = fields.Many2one(
        "calendar.event",
        string="Horario (Evento)",
        required=True,
        ondelete="cascade",
        index=True,
        auto_join=True,
    )

   
    name = fields.Char(string="Servicio", related="event_id.name", store=True, readonly=False)
    active = fields.Boolean(related="event_id.active", store=True, readonly=False)
    company_id = fields.Many2one("res.company", related="monitor_id.company_id", store=True, readonly=True)
    user_id = fields.Many2one("res.users", related="monitor_id.user_id", store=True, readonly=False)

   
    description = fields.Text(string="Descripción")
    age_range = fields.Selection(
        selection=[
            ("0_2", "0-2"),
            ("3_5", "3-5"),
            ("6_8", "6-8"),
            ("9_11", "9-11"),
        ],
        string="Rango de edad",
        required=True,
        default="0_2",
    )

    
    monitor_name = fields.Char(string="Nombre monitor/a", related="monitor_id.name", store=True, readonly=True)
