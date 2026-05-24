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
