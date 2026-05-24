## 🚀 Installation

Before using wap-kitty, install the dependencies and symlink the command:

```bash
# Install M3 engine (Google Material Color Utilities)
pip install --user --break-system-packages material-color-utilities

# Symlink the wap command
ln -sf ~/Downloads/wap-kitty/wap ~/.local/bin/wap

# Verify PATH
echo $PATH  # should contain ~/.local/bin
```

### Check kitty.conf

Make sure `~/.config/kitty/kitty.conf` includes:

```conf
include current-theme.conf
```

Without this line, Kitty won't load the generated theme.

---

# 🐱 noćtalia (niri) + wap-kitty

Automatically match your Kitty terminal colors to your niri wallpaper.

## 🔍 Detection

Reads `~/.cache/noctalia/wallpapers.json`.

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

Pre-configured via systemd:

```bash
systemctl --user status wall-theme.path
```

To enable manually:

```bash
cp ~/Downloads/wap-kitty/systemd/* ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now wap-kitty.path
```

## ✅ Verify

```bash
wap
```
