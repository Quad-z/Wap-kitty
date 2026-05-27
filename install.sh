#!/usr/bin/env bash
set -euo pipefail

if ! python3 -c "import material_color_utilities" 2>/dev/null; then
    python3 -m pip install --user --break-system-packages material-color-utilities
fi

ln -sf "$(pwd)/wap" ~/.local/bin/wap
ln -sf "$(pwd)/wap" ~/.local/bin/wall-theme

echo "Installed. Run: wap [image]"
echo ""
echo "Auto-detect supports: KDE, GNOME, Hyprland, Sway, XFCE,"
echo "  Cinnamon, MATE, noćtalia, feh, nitrogen, swww, macOS, Windows"
echo ""
echo "For auto-apply on wallpaper change, set up a systemd path unit:" 
echo "  https://github.com/quadraz/wap-kitty#auto-apply"
