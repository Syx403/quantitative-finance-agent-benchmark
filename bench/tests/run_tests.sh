#!/usr/bin/env bash
# Run the curated offline suite, or pass explicit pytest arguments.
set -euo pipefail
TASK_REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
TASK_PYTHON="${PYTHON:-$TASK_REPO_ROOT/.venv/bin/python}"
cd "$TASK_REPO_ROOT"
exec "$TASK_PYTHON" -m pytest -q "$@"
