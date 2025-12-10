from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Nomina(models.Model):
    _name = "nomina.nomina"
    _description = "Nómina de Empleado"
    _order = "fecha desc, empleado_id"

    name = fields.Char(
        string="Referencia",
        readonly=True,
        default=lambda self: "Nueva"
    )

    empleado_id = fields.Many2one(
        comodel_name="nomina.empleado",
        string="Empleado",
        required=True
    )

    fecha = fields.Date(
        string="Fecha",
        required=True,
        default=fields.Date.context_today
    )

    sueldo_base = fields.Float(
        string="Sueldo base",
        required=True
    )

    linea_ids = fields.One2many(
        comodel_name="nomina.linea",
        inverse_name="nomina_id",
        string="Bonificaciones y Deducciones"
    )

    total_bonificaciones = fields.Float(
        string="Total bonificaciones",
        compute="_compute_totales",
        store=True
    )

    total_deducciones = fields.Float(
        string="Total deducciones",
        compute="_compute_totales",
        store=True
    )

    irpf_porcentaje = fields.Float(
        string="IRPF (%)",
        required=True
    )

    irpf_pagado = fields.Float(
        string="IRPF pagado (€)",
        compute="_compute_irpf",
        store=True
    )

    sueldo_bruto = fields.Float(
        string="Sueldo bruto (base + bonificaciones)",
        compute="_compute_irpf",
        store=True
    )

    sueldo_neto = fields.Float(
        string="Sueldo neto (aprox.)",
        compute="_compute_sueldo_neto",
        store=True
    )

    justificante_pdf = fields.Binary(
        string="Justificante de transferencia (PDF)"
    )
    justificante_filename = fields.Char(
        string="Nombre del archivo"
    )

    estado = fields.Selection(
        selection=[
            ("redactada", "Redactada"),
            ("confirmada", "Confirmada"),
            ("pagada", "Pagada"),
        ],
        string="Estado",
        default="redactada",
        required=True
    )

    @api.model
    def create(self, vals):
        if vals.get("name", "Nueva") == "Nueva":
            seq = self.env["ir.sequence"].next_by_code("nomina.nomina") or "SIN-SEQ"
            vals["name"] = seq
        return super().create(vals)

    @api.depends("linea_ids", "linea_ids.importe_bruto", "linea_ids.tipo")
    def _compute_totales(self):
        for nomina in self:
            total_b = 0.0
            total_d = 0.0
            for linea in nomina.linea_ids:
                if linea.tipo == "bonificacion":
                    total_b += linea.importe_bruto
                else:
                    total_d += linea.importe_bruto
            nomina.total_bonificaciones = total_b
            nomina.total_deducciones = total_d

    @api.depends("sueldo_base", "total_bonificaciones", "irpf_porcentaje")
    def _compute_irpf(self):
        for nomina in self:
            bruto = nomina.sueldo_base + nomina.total_bonificaciones
            nomina.sueldo_bruto = bruto
            nomina.irpf_pagado = bruto * (nomina.irpf_porcentaje / 100.0) if nomina.irpf_porcentaje else 0.0

    @api.depends("sueldo_bruto", "total_deducciones", "irpf_pagado")
    def _compute_sueldo_neto(self):
        for nomina in self:
            nomina.sueldo_neto = nomina.sueldo_bruto - nomina.total_deducciones - nomina.irpf_pagado

    @api.constrains("sueldo_base", "irpf_porcentaje")
    def _check_valores_nomina(self):
        for nomina in self:
            if nomina.sueldo_base < 0:
                raise ValidationError("El sueldo base no puede ser negativo.")
            if nomina.irpf_porcentaje < 0 or nomina.irpf_porcentaje > 100:
                raise ValidationError("El IRPF debe estar entre 0 y 100.")


class NominaLinea(models.Model):
    _name = "nomina.linea"
    _description = "Línea de bonificación o deducción"

    nomina_id = fields.Many2one(
        comodel_name="nomina.nomina",
        string="Nómina",
        required=True,
        ondelete="cascade"
    )

    tipo = fields.Selection(
        selection=[
            ("bonificacion", "Bonificación"),
            ("deduccion", "Deducción"),
        ],
        string="Tipo",
        required=True,
        default="bonificacion"
    )

    importe_bruto = fields.Float(
        string="Importe bruto",
        required=True
    )

    concepto = fields.Char(
        string="Concepto",
        required=True
    )

    @api.constrains("importe_bruto")
    def _check_importe(self):
        for linea in self:
            if linea.importe_bruto < 0:
                raise ValidationError("El importe bruto no puede ser negativo.")
