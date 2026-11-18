# Puerta 01 · Brújula Bash

**Tiempo de referencia:** 40 min. Cambia de persona al teclado al menos una vez.

## Desafío

Abre Git Bash **en la carpeta raíz del juego**. Sin utilizar el explorador de Windows, averigua dónde estás y encuentra el archivo oculto del sector 01.

```bash
pwd
ls -la
cat COMIENZA_AQUI.txt
cd sector_01
ls -la
```

**Pregunta:** ¿qué cambia entre `ls` y `ls -la`? ¿En qué carpeta está la pista?

Cuando la localices, copia el archivo secreto como `evidencias/01_bash.txt` (puedes usar `cp` o `cat ... > ...`). Regresa a la raíz y ejecuta `bash desbloquear.sh 1`.

**Prueba de aprendizaje:** cada persona explica qué significa `pwd`, `cd`, `cat` y cómo identificar archivos ocultos.

## Pistas graduadas

- [Pista 1](PISTA_1.md): orientación sin dar la respuesta.
- [Pista 2](PISTA_2.md): ayuda más explícita.

**Siguiente puerta:** [Sala 02](../02-git/INSTRUCCIONES.md).
