#!/usr/bin/env bash
# Guía formativa, no sistema de seguridad. Ejecutar desde cualquier carpeta.
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT" || exit 1
NUM="${1:-}"

error() { printf '\nPENDIENTE: %s\n' "$1" >&2; exit 1; }
correcto() {
  mkdir -p .roomscape
  printf 'Puerta %s completada | equipo local\n' "$NUM" >> .roomscape/progreso.log
  printf '\n✔ PUERTA %s COMPLETADA. %s\n' "$NUM" "$1"
  if [[ "$NUM" =~ ^[1-5]$ ]]; then
    siguiente=$((10#$NUM + 1))
    ruta=$(printf 'salas/%02d-' "$siguiente")
    for f in "${ruta}"*/INSTRUCCIONES.md; do
      if [[ -f "$f" ]]; then
        printf 'Siguiente misión: %s\n' "$f"
      fi
    done
  else
    printf 'Ciudad Métrica recuperada. Abre CIERRE.md.\n'
  fi
}

[[ "$NUM" =~ ^[1-6]$ ]] || error 'Uso: bash desbloquear.sh N, con N de 1 a 6.'

case "$NUM" in
  1)
    [[ -s evidencias/01_bash.txt ]] || error 'Falta evidencias/01_bash.txt: encuentra la pista oculta y cópiala.'
    grep -q 'PODER-01-BRUJULA' evidencias/01_bash.txt || error 'No es la pista correcta: busca con ls -la.'
    correcto 'Sabes explorar carpetas y archivos ocultos.'
    ;;
  2)
    [[ -d mi-primer-repo/.git ]] || error 'Falta un repositorio Git en mi-primer-repo/.'
    [[ -s mi-primer-repo/README.md ]] || error 'Falta un README.md propio en mi-primer-repo/.'
    git -C mi-primer-repo log -1 --format=%h >/dev/null 2>&1 || error 'Falta un commit. Revisa git status, git add y git commit.'
    correcto 'Un commit local preserva la historia. Publicar es opcional hoy.'
    ;;
  3)
    [[ -s evidencias/bitacora.md ]] || error 'Guarda evidencias/bitacora.md desde Sublime Text.'
    grep -q '^## Hallazgo' evidencias/bitacora.md || error 'Falta la sección ## Hallazgo.'
    grep -q '^## Pregunta' evidencias/bitacora.md || error 'Falta la sección ## Pregunta.'
    [[ $(wc -c < evidencias/bitacora.md) -gt 90 ]] || error 'Amplía el hallazgo y la pregunta con contenido propio.'
    correcto 'El conocimiento ya está documentado en Markdown.'
    ;;
  4)
    [[ -s evidencias/mapa_editor.md ]] || error 'Guarda evidencias/mapa_editor.md desde VS Code.'
    grep -qi 'VS Code' evidencias/mapa_editor.md || error 'Describe VS Code en el mapa.'
    grep -qi 'Python' evidencias/mapa_editor.md || error 'Incluye Python en el mapa.'
    grep -q 'datos/' evidencias/mapa_editor.md || error 'Identifica la carpeta datos/.'
    grep -q 'scripts/' evidencias/mapa_editor.md || error 'Identifica la carpeta scripts/.'
    correcto 'Sabes organizar y navegar un proyecto.'
    ;;
  5|6)
    PYTHON=""
    for command in python python3; do
      if command -v "$command" >/dev/null 2>&1; then
        PYTHON="$command"
        break
      fi
    done
    if [[ -z "$PYTHON" ]] && command -v py >/dev/null 2>&1; then
      PYTHON="py"
    fi
    [[ -n "$PYTHON" ]] || error 'Python no está disponible en Git Bash; revisa la instalación y PATH.'
    if [[ "$PYTHON" = 'py' ]]; then
      py -3.13 scripts/verificar.py "$NUM" || error 'Revisa la evidencia con la pista de la sala.'
    else
      "$PYTHON" scripts/verificar.py "$NUM" || error 'Revisa la evidencia con la pista de la sala.'
    fi
    if [[ "$NUM" = 5 ]]; then
      correcto 'Ya distingues una operación de un ingreso.'
    else
      correcto 'Has explicado el resultado y sus límites. El docente revisará el razonamiento.'
    fi
    ;;
esac
