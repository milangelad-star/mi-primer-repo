# Diccionario de datos · CSV sintético

| Campo | Tipo | Descripción |
|---|---|---|
| `id_operacion` | texto | Identificador ficticio de cada operación; sin nombres ni datos reales |
| `fecha` | fecha ISO | Fecha de registro de la operación |
| `canal` | categoría | web, app o tienda |
| `estado` | categoría | `completada`, `cancelada` o `devuelta` |
| `importe_eur` | decimal con punto | Importe asociado a la operación |

**Interpretación para esta simulación:** `completada` es operación finalizada con ingreso; `cancelada` no genera ingreso; `devuelta` describe una operación reembolsada cuyo valor no se incorpora como ingreso neto final. **No hay doble registro de una venta y su devolución en filas separadas.** Esto es una convención simplificada y no sustituye un modelo contable real con ajustes, impuestos, comisiones y fecha de reconocimiento.

Los datos son totalmente **sintéticos** y no representan el desempeño de ninguna organización.
