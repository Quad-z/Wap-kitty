# 🧉 MATE + wap-kitty

Automatically match your Kitty terminal colors to your MATE wallpaper.

## 🔍 Detection

Reads `gsettings get org.mate.desktop.background picture-filename`.

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

Create `~/Downloads/wap-kitty/mate-watcher.sh`:

```bash
#!/bin/bash
while true; do
  gsettings monitor org.mate.desktop.background picture-filename | while read -r line; do
    wap
  done
done
```

```bash
chmod +x ~/Downloads/wap-kitty/mate-watcher.sh
```

Add to autostart via **System → Preferences → Startup Applications**.

## ✅ Verify

```bash
wap
```
