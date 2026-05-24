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

# 🌿 nitrogen + wap-kitty

Automatically match your Kitty terminal colors when using nitrogen.

## 🔍 Detection

Reads `~/.config/nitrogen/bg-saved.cfg`, field `file=`.

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

Append `wap` to your wallpaper script:

```bash
#!/bin/bash
nitrogen --set-zoom-fill "$1"
wap
```

## ✅ Verify

```bash
wap
```
