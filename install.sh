#!/usr/bin/env bash
set -euo pipefail

if ! python3 -c "import material_color_utilities" 2>/dev/null; then
    python3 -m pip install --user --break-system-packages material-color-utilities
fi

ln -sf "$(pwd)/wap" ~/.local/bin/wap
ln -sf "$(pwd)/wap" ~/.local/bin/wall-theme

echo "Installed. Run: wap [image]"
