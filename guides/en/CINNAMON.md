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

# 🥮 Cinnamon + wap-kitty

Automatically match your Kitty terminal colors to your Cinnamon wallpaper.

## 🔍 Detection

Reads `gsettings get org.cinnamon.desktop.background picture-uri`.

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

Create `~/Downloads/wap-kitty/cinnamon-watcher.sh`:

```bash
#!/bin/bash
while true; do
  gsettings monitor org.cinnamon.desktop.background picture-uri | while read -r line; do
    wap
  done
done
```

```bash
chmod +x ~/Downloads/wap-kitty/cinnamon-watcher.sh
```

Add to autostart via **Preferences → Startup Applications**.

## ✅ Verify

```bash
wap
```
