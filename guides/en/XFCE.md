# 🐭 XFCE + wap-kitty

Automatically match your Kitty terminal colors to your XFCE wallpaper.

## 🔍 Detection

Runs `xfconf-query -c xfce4-desktop -lv`, looks for `last-image` or `image-path`.

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

Create `~/Downloads/wap-kitty/xfce-watcher.sh`:

```bash
#!/bin/bash
while inotifywait -qe close_write "$HOME/.config/xfce4/desktop/..." 2>/dev/null; do
  wap
done
```

```bash
chmod +x ~/Downloads/wap-kitty/xfce-watcher.sh
```

Add to autostart via **Session and Startup → Application Autostart**.

## ✅ Verify

```bash
wap
```
