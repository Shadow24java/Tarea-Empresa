from odoo import models, fields, api
from odoo.exceptions import ValidationError

class DeclaracionRenta(models.Model):
    _name = "nomina.declaracion.renta"
    _description = "Declaración de la renta anual del empleado"
    _order = "anio desc, empleado_id"

    name = fields.Char(
        string="Referencia",
        compute="_compute_name",
        store=True
    )

    anio = fields.Integer(
        string="Año",
        required=True
    )

    empleado_id = fields.Many2one(
        comodel_name="nomina.empleado",
        string="Empleado",
        required=True
    )

    nomina_ids = fields.Many2many(
        comodel_name="nomina.nomina",
        relation="nomina_declaracion_rel",
        column1="declaracion_id",
        column2="nomina_id",
        string="Nóminas incluidas"
    )

    sueldo_bruto_total = fields.Float(
        string="Sueldo bruto total",
        compute="_compute_totales",
        store=True
    )

    impuestos_irpf_pagados = fields.Float(
        string="IRPF total pagado",
        compute="_compute_totales",
        store=True
    )

    @api.depends("anio", "empleado_id")
    def _compute_name(self):
        for decl in self:
            if decl.empleado_id and decl.anio:
                decl.name = f"Declaración {decl.anio} - {decl.empleado_id.name}"
            else:
                decl.name = "Nueva Declaración"

    @api.depends("nomina_ids", "nomina_ids.sueldo_bruto", "nomina_ids.irpf_pagado")
    def _compute_totales(self):
        for decl in self:
            bruto_total = 0.0
            irpf_total = 0.0
            for nomina in decl.nomina_ids:
                bruto_total += nomina.sueldo_bruto
                irpf_total += nomina.irpf_pagado
            decl.sueldo_bruto_total = bruto_total
            decl.impuestos_irpf_pagados = irpf_total

    @api.constrains("nomina_ids", "anio", "empleado_id")
    def _check_nominas(self):
        for decl in self:
            # Máximo 14 nóminas
            if len(decl.nomina_ids) > 14:
                raise ValidationError("Una declaración solo puede tener un máximo de 14 nóminas.")

            for nomina in decl.nomina_ids:
                if nomina.empleado_id != decl.empleado_id:
                    raise ValidationError("Todas las nóminas deben ser del mismo empleado.")
                if nomina.fecha and nomina.fecha.year != decl.anio:
                    raise ValidationError("Todas las nóminas deben pertenecer al mismo año natural de la declaración.")
