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

# 🗼 Sway + wap-kitty

Automatically match your Kitty terminal colors to your Sway wallpaper.

## 🔍 Detection

1. Runs `swaymsg -t get_outputs` (reads `current_wallpaper` field)
2. Falls back to scanning for `swaybg` process arguments

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

### Method 1: hook in swaybg launcher

```bash
#!/bin/bash
swaybg -i "$1" -m fill &
wap
```

### Method 2: timer in Sway config

Add to `~/.config/sway/config`:

```
exec_always --no-startup-id while true; do sleep 30; wap; done
```

## ✅ Verify

```bash
wap
```
