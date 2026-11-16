# 🦸 La Liga del Dato — Operación Ciudad Métrica

**Bootcamp Data Analyst · ARRABAL-AID / SOMOS F5**  
**Módulo 0 · Primer día · Roomscape de instalación**

> Doctor Ruido ha apagado los indicadores de Ciudad Métrica. En seis salas recuperaréis las rutas, la memoria, la documentación, el código y los resultados. No necesitáis conocimientos previos de programación.

## 0. Empieza aquí (sin instalar todo de golpe)

1. **Descarga la carpeta**: en GitHub pulsa **Code → Download ZIP**, descomprímela en una ruta sencilla, por ejemplo `Documentos/roomscape/`. No la ejecutes desde dentro del ZIP.
2. **Instala Git for Windows** (incluye **Git Bash**): [descarga oficial](https://git-scm.com/install/windows). Si ya lo tienes, ábrelo desde Inicio. En Windows Git Bash simula comandos Bash; **no es una distribución Linux**.
3. En el Explorador de Windows, abre la carpeta descomprimida, haz clic derecho y selecciona **Open Git Bash here** (si aparece); o abre Git Bash y accede a la ruta con `cd`.
4. Escribe `pwd`, luego `ls -la` y **`cat COMIENZA_AQUI.txt`**. Empieza por la sala 01.
5. Cada puerta termina con una evidencia. Para comprobarla escribe **`bash desbloquear.sh N`**, donde `N` es el número de puerta (del 1 al 6).

El progreso es **didáctico**, no un sistema de seguridad: las salas están incluidas en el ZIP para que se pueda trabajar sin conexión. Las pistas y el validador son visibles.

## 1. Descargas y accesos directos oficiales

**Instala en el momento de la puerta correspondiente**; no es obligatorio instalarlo todo antes de comenzar.

| Puerta | Herramienta | Enlace directo | ¿Para qué? | Verificación rápida |
|:--:|---|---|---|---|
| 01 | **Git for Windows / Git Bash** | [Descargar](https://git-scm.com/install/windows) | Terminal Bash y rutas | `pwd` / `git --version` |
| 02 | **GitHub (cuenta)** | [Crear cuenta gratuita](https://github.com/signup) / [entrar](https://github.com/login) | Publicar el primer repositorio personal | Acceso web y correo verificado |
| 03 | **Sublime Text** | [Descargar](https://www.sublimetext.com/download) | Editor de texto ligero (evaluación gratuita; licencia para uso continuado) | Abrir y guardar un `.md` |
| 04 | **Visual Studio Code** | [Descargar](https://code.visualstudio.com/Download) | Editor principal del curso | `code --version` si el comando está disponible |
| 04 | **Extensión Python (VS Code)** | [Instalar](https://marketplace.visualstudio.com/items?itemName=ms-python.python) | Soporte del lenguaje | Visible en Extensiones |
| 04 | **Extensión Pylance (VS Code)** | [Instalar](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) | Autocompletado y análisis | Visible en Extensiones |
| 05 | **Python 3.13.x, 64 bits** | [Descargas Python](https://www.python.org/downloads/) / [rama 3.13](https://www.python.org/downloads/release/python-31317/) | Ejecutar el primer script | `py -3.13 --version` |
| 06 | **Extensión Jupyter (VS Code)** | [Instalar](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) | Abrir y ejecutar `.ipynb` | Notebook abre en VS Code |
| 06 | **ipykernel (paquete Python)** | [Documentación](https://ipykernel.readthedocs.io/en/stable/install.html) | Kernel de ejecución | `python -m pip show ipykernel` |

**De apoyo, no requeridas para superar las seis puertas:**

| Herramienta | Acceso oficial | Papel en el bootcamp |
|---|---|---|
| [GitHub Desktop](https://desktop.github.com/) | Descargar aplicación | Interfaz gráfica opcional para Git; la sala 02 usa terminal |
| [Google Colab](https://colab.research.google.com/) | Abrir en navegador | Plan B si un equipo no puede ejecutar el notebook en local |
| [Power BI Desktop](https://learn.microsoft.com/es-es/power-bi/fundamentals/desktop-get-the-desktop) | Descargar / Store | BI principal; **no es puerta obligatoria el primer día** |
| [DBeaver Community](https://dbeaver.io/download/) | Descargar aplicación | SQL y bases de datos en sesiones posteriores |
| [Postman](https://www.postman.com/downloads/) | Descargar aplicación | Probar APIs más adelante |
| [Streamlit](https://docs.streamlit.io/get-started/installation) | Instrucciones de instalación | Apps de datos en módulos posteriores |

**No instalamos hoy:** Docker, Conda, R, PyCharm, Tableau Public ni herramientas de IA por obligación. Tampoco se usa Microsoft Excel en este itinerario. Si alguien ya tiene alguna instalada no necesita desinstalarla.

## 2. Mapa de las salas

| Puerta | Misión | Abre este archivo | Evidencia que debe producirse |
|:--:|---|---|---|
| 01 | 🧭 **Brújula Bash** — Encontrar | [`salas/01-bash/INSTRUCCIONES.md`](salas/01-bash/INSTRUCCIONES.md) | `evidencias/01_bash.txt` |
| 02 | 🛡️ **Escudo Git** — Versionar | [`salas/02-git/INSTRUCCIONES.md`](salas/02-git/INSTRUCCIONES.md) | Un commit en `mi-primer-repo/` |
| 03 | ✒️ **Pluma Sublime** — Documentar | [`salas/03-sublime/INSTRUCCIONES.md`](salas/03-sublime/INSTRUCCIONES.md) | `evidencias/bitacora.md` |
| 04 | 🔎 **Visor VS Code** — Organizar | [`salas/04-vscode/INSTRUCCIONES.md`](salas/04-vscode/INSTRUCCIONES.md) | `evidencias/mapa_editor.md` |
| 05 | ⚙️ **Motor Python** — Calcular | [`salas/05-python/INSTRUCCIONES.md`](salas/05-python/INSTRUCCIONES.md) | `evidencias/informe.txt` |
| 06 | 🔮 **Oráculo Jupyter** — Explicar | [`salas/06-jupyter/INSTRUCCIONES.md`](salas/06-jupyter/INSTRUCCIONES.md) | Notebook ejecutado y dos frases de interpretación |

Las pistas están **dentro de cada sala** en `PISTA_1.md` y `PISTA_2.md`. Usa la primera solo si la necesitáis y la segunda después de intentar resolver el reto.

## 3. Equipos y turnos

Somos **22 personas en 6 equipos**: cuatro grupos de cuatro y dos de tres. Cada equipo usa **una copia local independiente** del juego; elegid vuestra tarjeta en [`equipos/`](equipos/ASIGNACION.md). Cambiad periódicamente quién controla el teclado y quién explica, verifica o documenta. No importa quién termina primero: toda persona debe poder explicar la evidencia.

## 4. Reglas del juego y privacidad

- Trabajamos con un **CSV sintético**, no con datos personales reales.
- **No publiques** el ZIP del juego, el dataset del roomscape, las pistas, tokens, contraseñas ni el directorio `evidencias/` en tu repositorio personal.
- Para la sala 02, el repositorio **`mi-primer-repo` es nuevo y separado**, creado dentro de esta carpeta a efectos del ejercicio. Solo tendrá un README propio.
- Si GitHub pide iniciar sesión, resolver CAPTCHA o verificar el correo, **no bloquees al resto del equipo**: el commit local es la evidencia mínima; el `push` se hace cuando se pueda.
- No borres archivos originales del roomscape. Modifica solo los entregables indicados.

## 5. Si algo falla

- **No aparece `git` en PowerShell:** utiliza Git Bash, abre una nueva terminal tras instalar Git y verifica `git --version`.
- **No aparece `py -3.13`:** verifica la instalación de Python 3.13 de 64 bits. Si falla el launcher `py`, usa `python --version` y comprueba que sea 3.13.x. Para ejecutar `desbloquear.sh 5`/`6` utiliza una instalación que permita `python3` o `python` en Git Bash.
- **`code` no existe:** abre VS Code desde Inicio y usa **Archivo → Abrir carpeta**; no es obligatorio el comando `code`.
- **Notebook sin kernel:** crea el entorno de la sala 06 e instala `ipykernel` desde ese mismo entorno.
- **Error al instalar paquetes por red:** pide ayuda al docente; se permite explicar la resolución mientras se tramita la incidencia.
- **El script indica “pendiente”:** vuelve a la instrucción de la sala; no modifiques el validador para que diga aprobado.

## 6. Cierre

Al completar la puerta 06, cada equipo explica **cuántas operaciones hay**, **cuántas están completadas**, **qué cifra considera ingresos** y **qué no se puede deducir del CSV**. El ticket de salida está en [`CIERRE.md`](CIERRE.md).

> Material de aula ARRABAL-AID / SOMOS F5. Código y dataset sintéticos, con fines formativos. Los enlaces externos llevan a sus respectivos proveedores.
# mi-primer-repo
