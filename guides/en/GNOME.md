# 🐚 GNOME + wap-kitty

Automatically match your Kitty terminal colors to your GNOME wallpaper.

## 🔍 Detection

Reads wallpaper from gsettings:
```bash
gsettings get org.gnome.desktop.background picture-uri-dark
```
Falls back to `picture-uri`.

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

Create `~/Downloads/wap-kitty/gnome-watcher.sh`:

```bash
#!/bin/bash
while true; do
  gsettings monitor org.gnome.desktop.background picture-uri-dark | while read -r line; do
    wap
  done
done
```

```bash
chmod +x ~/Downloads/wap-kitty/gnome-watcher.sh
```

Add to autostart:
- Via `gnome-session-properties`
- Or place a `.desktop` file in `~/.config/autostart/`

## ✅ Verify

```bash
wap
```
