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
