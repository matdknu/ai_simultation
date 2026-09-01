#!/usr/bin/env bash
# Cross the Wall — launcher (siempre desde crossthewall/, venv incluido)
set -e
cd "$(dirname "$0")"

if [ ! -d .venv ]; then
  echo "→ Creando entorno virtual..."
  python3 -m venv .venv
  .venv/bin/pip install -r requirements.txt
fi

exec .venv/bin/python main.py "$@"
