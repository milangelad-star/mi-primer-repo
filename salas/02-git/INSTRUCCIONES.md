# Puerta 02 · Escudo Git

**Tiempo de referencia:** 60 min. Cambia de persona al teclado al menos una vez.

## Desafío

Un informe sin historial es difícil de auditar. Crea **un repositorio nuevo dentro de `mi-primer-repo/`**, separado de los archivos del juego.

```bash
mkdir mi-primer-repo
cd mi-primer-repo
git init -b main
printf '# Mi primer repositorio\\n\\nAprenderé a explicar decisiones con datos.\\n' > README.md
git status
git add README.md
git commit -m 'Mi primer commit'
git log -1 --oneline
cd ..
```

Antes del commit puede que necesites configurar tu identidad local con `git config --global user.name` y `git config --global user.email` usando **tus datos y tu propio correo** (si lo necesitas, pregunta al docente). No anotes el correo en un fichero del juego.

Comprueba `bash desbloquear.sh 2`. Después, si tu cuenta y la red funcionan, crea un **repositorio público vacío** en [GitHub](https://github.com/new), sin README generado, y añade el remoto siguiendo **la URL exacta que te proporciona GitHub**. No hace falta publicar para superar la puerta.

**Nunca subas la carpeta del roomscape como tu primer repositorio personal.**

**Prueba de aprendizaje:** cada persona explica en qué se diferencian `add`, `commit`, `push` y el historial local/remoto.

## Pistas graduadas

* [Pista 1](PISTA_1.md): orientación sin dar la respuesta.
* [Pista 2](PISTA_2.md): ayuda más explícita.

**Siguiente puerta:** [Sala 03](../03-sublime/INSTRUCCIONES.md).

