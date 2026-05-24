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
