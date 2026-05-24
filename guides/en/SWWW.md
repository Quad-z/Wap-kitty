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

# 🌊 swww + wap-kitty

Automatically match your Kitty terminal colors when using swww.

## 🔍 Detection

Runs `swww query` and parses `image: "..."` from output.

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

Append `wap` to your wallpaper script:

```bash
#!/bin/bash
swww img "$1"
wap
```

## ✅ Verify

```bash
wap
```
