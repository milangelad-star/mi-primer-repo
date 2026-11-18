# Puerta 05 · Motor Python

**Tiempo de referencia:** 40 min. Cambia de persona al teclado al menos una vez.

## Desafío

Doctor Ruido afirma que **toda operación equivale a un ingreso**. Verifica si eso es correcto.

1. Consulta `datos/operaciones.csv` en VS Code. Contiene operaciones ficticias con estados `completada`, `cancelada` y `devuelta`.
2. Abre `scripts/analizar_operaciones.py`. Hay una **línea intencionadamente incorrecta** identificada como `RETO`; corrígela para que solo cuenten como ingresos las operaciones **completadas**.
3. Ejecuta desde la raíz:

```bash
py -3.13 --version
py -3.13 scripts/analizar_operaciones.py
cat evidencias/informe.txt
```

Si en Git Bash no está disponible el lanzador `py`, comprueba que `python --version` muestra 3.13.x y ejecuta `python scripts/analizar_operaciones.py`.

4. Explica por qué no corresponde sumar las cancelaciones o devoluciones a la cifra de ingresos. Ejecuta `bash desbloquear.sh 5`.

**No necesitamos pandas en esta sala:** usamos la biblioteca estándar para centrarnos en el significado del indicador.

## Pistas graduadas

- [Pista 1](PISTA_1.md): orientación sin dar la respuesta.
- [Pista 2](PISTA_2.md): ayuda más explícita.

**Siguiente puerta:** [Sala 06](../06-jupyter/INSTRUCCIONES.md).
