Módulo Odoo — Gestión de PCs de Empresa (pc_management)

Descripción General
El módulo "pc_management" permite gestionar los ordenadores de una empresa, componentes, usuarios asignados y los sistemas operativos instalados mediante un sistema de etiquetas.

Utilizando modelos personalizados, relaciones Many2one y Many2many, campos calculados, validaciones, vistas y menús propios.

El objetivo es tener un inventario claro y bien estructurado enfocado a la informática.

Funcionalidades Principales

- Registrar componentes informáticos con precio y especificaciones.
- Registrar ordenadores con información del usuario asignado.
- Asignar múltiples componentes a cada ordenador.
- Añadir sistemas operativos mediante etiquetas (tags).
- Calcular automáticamente el precio total del ordenador.
- Evitar errores introduciendo fechas futuras.
- Menú completo con acceso a Ordenadores, Componentes y Tags.
- Permisos configurados para usuarios internos.

Estructura del Módulo

Modelos Implementados

1. "pc.component"
Representa componentes reutilizables (RAM, CPU, SSD…)
- "nombre"
- "especificaciones"
- "precio" (Monetary)
- "currency_id" (Many2one obligatorio)


2. "pc.ordenador"
Registra la información principal del ordenador.
- "numero_equipo2"
- "user_id" → *Many2one a res.users*
- "components_ids" → *Many2many a pc.component*
- "ultima_mod"
- "precio_total" (campo calculado)
- "incidencias"
- "tags" → *Many2many a pc.tags*
- "currency_id"

Incluye:
- Validación que evita fechas futuras
- Cálculo automático del precio total


3. "pc.tags"
Tabla auxiliar para añadir etiquetas de sistemas operativos.
- "name"


Relaciones del Módulo

Many2one
"pc.ordenador.user_id" → "res.users" 
Un ordenador pertenece a un único usuario, pero un usuario puede tener varios ordenadores.

Many2many
"pc.ordenador.components_ids" → "pc.component" 
Un ordenador puede tener muchos componentes, y un componente puede estar en varios ordenadores.

"pc.ordenador.tags" → "pc.tags"  
Un ordenador puede tener varios sistemas operativos (Windows, Linux…).

Monetary + Many2one obligatorio
"precio" y "precio_total" requieren "currency_id".


Funcionamiento Dentro de Odoo

Menú Principal
El módulo crea un menú llamado Gestión de PCs con:
- Ordenadores
- Componentes
- Tags

Crear Componentes
Desde el menú "Componentes" puedes registrar cada componente reutilizable.  
Cada componente incluye su nombre, especificaciones y precio.

Crear Tags
Permite crear etiquetas como:
- Windows 10  
- Ubuntu 22.04  
- Windows 11  
- Linux Mint  

Estas etiquetas se usan en los ordenadores.

Crear Ordenadores
Se registra un ordenador con:
- Usuario asignado
- Componentes instalados
- Tags (Sistemas Operativos)
- Fecha de última modificación
- Incidencias

Odoo calcula automáticamente el precio total sumando todos los componentes asignados.
