import re

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    dni = fields.Char(string="DNI", copy=False)
    nss = fields.Char(string="Nº Seguridad Social", copy=False)

    @api.constrains("dni", "nss")
    def _check_dni_nss(self):
        """
        Verificación:
        - Ambos campos deben estar rellenos.
        - NSS: 12 dígitos (2 provincia + 8 identificativos + 2 control).
        - DNI: 8 dígitos + 1 letra de control (mapeada por mod 23).
        """
        letters = "TRWAGMYFPDXBNJZSQVHLCKE"

        for emp in self:
            
            if not emp.dni or not emp.nss:
                raise ValidationError("Debes rellenar DNI y NSS para el empleado.")

            
            dni = emp.dni.strip().upper().replace(" ", "").replace("-", "")
            if not re.fullmatch(r"\d{8}[A-Z]", dni):
                raise ValidationError("DNI inválido. Formato: 8 dígitos y 1 letra (ej: 12345678Z).")

            number = int(dni[:8])
            letter = dni[8]
            expected_letter = letters[number % 23]
            if letter != expected_letter:
                raise ValidationError(
                    f"DNI inválido. Letra de control incorrecta (debería ser {expected_letter})."
                )

           
            nss = emp.nss.strip().replace(" ", "").replace("-", "")
            if not re.fullmatch(r"\d{12}", nss):
                raise ValidationError("NSS inválido. Debe tener exactamente 12 dígitos.")

            
            base = int(nss[:10])
            control = nss[10:]
            expected_control = str(base % 97).zfill(2)
            if control != expected_control:
                raise ValidationError(
                    f"NSS inválido. Dígitos de control incorrectos (debería terminar en {expected_control})."
                )
