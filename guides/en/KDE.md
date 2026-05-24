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

# 🌀 KDE Plasma + wap-kitty

Automatically match your Kitty terminal colors to your KDE wallpaper.

## 🔍 Detection

Parses `~/.config/plasma-org.kde.plasma.desktop-appletsrc` for `Image=/path/to/wallpaper`.

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

### Method: script in KDE Autostart

1. Open **System Settings → Autostart**
2. Click **Add → Local Script**
3. Point to `~/Downloads/wap-kitty/kde-watcher.sh`

Create `~/Downloads/wap-kitty/kde-watcher.sh`:

```bash
#!/bin/bash
while inotifywait -qe close_write "$HOME/.config/plasma-org.kde.plasma.desktop-appletsrc"; do
  wap
done
```

```bash
chmod +x ~/Downloads/wap-kitty/kde-watcher.sh
```

## ✅ Verify

```bash
wap
```
