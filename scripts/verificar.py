"""Validación formativa: usa la misma fuente, sin respuestas fijas embebidas."""
import csv
from decimal import Decimal
import json
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parents[1]


def revisar_05():
    informe = RAIZ / 'evidencias' / 'informe.txt'
    if not informe.is_file():
        return False, 'Falta evidencias/informe.txt. Ejecuta el script de Python.'
    with (RAIZ / 'datos' / 'operaciones.csv').open(encoding='utf-8', newline='') as f:
        filas = list(csv.DictReader(f))
    total = len(filas)
    completadas = sum(f['estado'] == 'completada' for f in filas)
    canceladas = sum(f['estado'] == 'cancelada' for f in filas)
    devueltas = sum(f['estado'] == 'devuelta' for f in filas)
    ingresos = sum((Decimal(f['importe_eur']) for f in filas if f['estado'] == 'completada'), Decimal('0.00'))
    texto = informe.read_text(encoding='utf-8')
    esperadas = [f'Operaciones totales: {total}', f'Completadas: {completadas}',
                 f'Canceladas: {canceladas}', f'Devueltas: {devueltas}',
                 f'Ingresos completados (EUR): {ingresos:.2f}']
    faltan = [e for e in esperadas if e not in texto]
    if faltan:
        return False, 'El informe no cumple todas las comprobaciones; revisa el filtro de estados.'
    return True, 'Informe correcto: has distinguido ingresos de operaciones no completadas.'


def revisar_06():
    ok, mensaje = revisar_05()
    if not ok:
        return False, 'La sala 06 requiere una sala 05 válida. ' + mensaje
    destino = RAIZ / 'notebooks' / 'cuaderno_heroe.ipynb'
    try:
        notebook = json.loads(destino.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        return False, 'No encuentro un notebook válido. Guarda el archivo .ipynb.'
    celdas = notebook.get('cells', [])
    codigo = [c for c in celdas if c.get('cell_type') == 'code']
    if not codigo or not all(c.get('execution_count') is not None for c in codigo):
        return False, 'Ejecuta todas las celdas de código y guarda el notebook.'
    finales = [c for c in celdas if c.get('cell_type') == 'markdown' and 'Interpretación' in ''.join(c.get('source', []))]
    if not finales:
        return False, 'Falta la celda Markdown de Interpretación.'
    texto = ''.join(finales[-1].get('source', []))
    if 'COMPLETAR' in texto.upper():
        return False, 'Sustituye COMPLETAR por dos frases propias en la celda final.'
    lineas = [line.strip(' -*	') for line in texto.splitlines() if line.strip() and not line.startswith('#')]
    if len(lineas) < 2 or sum(len(s) >= 25 for s in lineas) < 2:
        return False, 'Escribe al menos dos frases interpretativas, no solo títulos o etiquetas.'
    return True, 'Notebook ejecutado y dos interpretaciones documentadas. El docente debe revisar su calidad.'


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('5', '6'):
        print('Uso: python scripts/verificar.py 5|6', file=sys.stderr)
        sys.exit(2)
    correcto, texto = (revisar_05() if sys.argv[1] == '5' else revisar_06())
    print(('OK: ' if correcto else 'PENDIENTE: ') + texto)
    sys.exit(0 if correcto else 1)
