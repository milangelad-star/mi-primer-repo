# Puerta 06 · Oráculo Jupyter

**Tiempo de referencia:** 40 min. Cambia de persona al teclado al menos una vez.

## Desafío

Convertir números en decisiones exige un análisis **reproducible** y una interpretación explícita.

Desde Git Bash, situándote en la raíz del juego:

```bash
py -3.13 -m venv .venv
source .venv/Scripts/activate
python -m pip install ipykernel
```

En equipos donde `py -3.13` no esté disponible, comprueba que `python --version` es 3.13.x antes de usar `python -m venv .venv`. No usamos Conda ni un servidor Jupyter independiente.

1. En VS Code instala la extensión **Jupyter** y abre `notebooks/cuaderno_heroe.ipynb`.
2. Selecciona el kernel del entorno `.venv`.
3. Ejecuta las celdas en orden (**Run All**). Comprueba que muestran totales coherentes con `evidencias/informe.txt`.
4. En la celda final de Markdown sustituye **`COMPLETAR`** por **al menos dos frases propias**: una que interprete los ingresos y otra que explique **un límite** del CSV. Guarda el notebook (Ctrl+S).
5. Vuelve a la raíz en Git Bash y ejecuta `bash desbloquear.sh 6`.

**Prueba de aprendizaje:** distinguir entre celda de código, celda Markdown y kernel; justificar un KPI y reconocer qué no puede concluirse con esa muestra.

## Pistas graduadas

- [Pista 1](PISTA_1.md): orientación sin dar la respuesta.
- [Pista 2](PISTA_2.md): ayuda más explícita.

**Última puerta:** completa el [ticket de salida](../../CIERRE.md).
