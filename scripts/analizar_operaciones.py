"""Puerta 05: primer análisis con CSV sintético y biblioteca estándar."""
from collections import Counter
import csv
from decimal import Decimal
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
ORIGEN = RAIZ / "datos" / "operaciones.csv"
DESTINO = RAIZ / "evidencias" / "informe.txt"

# RETO: Doctor Ruido ha introducido un criterio de ingresos equivocado.
# Corrige SOLO esta línea después de leer los estados del CSV.
ESTADOS_QUE_CUENTAN_COMO_INGRESOS = {"completada"}


def analizar():
    with ORIGEN.open(encoding="utf-8", newline="") as fichero:
        operaciones = list(csv.DictReader(fichero))

    conteos = Counter(fila["estado"] for fila in operaciones)
    ingresos = sum(
        (Decimal(fila["importe_eur"]) for fila in operaciones
         if fila["estado"] in ESTADOS_QUE_CUENTAN_COMO_INGRESOS),
        Decimal("0.00"),
    )
    DESTINO.parent.mkdir(exist_ok=True)
    informe = (
        "INFORME DE CIUDAD METRICA\n"
        f"Operaciones totales: {len(operaciones)}\n"
        f"Completadas: {conteos['completada']}\n"
        f"Canceladas: {conteos['cancelada']}\n"
        f"Devueltas: {conteos['devuelta']}\n"
        f"Ingresos completados (EUR): {ingresos:.2f}\n"
    )
    DESTINO.write_text(informe, encoding="utf-8")
    print(informe)
    return informe


if __name__ == "__main__":
    analizar()
