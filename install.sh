#!/bin/bash

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
pushd "$SCRIPT_DIR/.." || exit

python3 -m venv venv
source venv/bin/activate

pip install -e .

deactivate

echo "Installation complete."

popd || exit