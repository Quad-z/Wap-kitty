# 🦎 Hyprland + wap-kitty

Automatically match your Kitty terminal colors to your Hyprland wallpaper.

## 🔍 Detection

1. Runs `hyprctl hyprpaper listloaded`
2. Falls back to parsing `~/.config/hypr/hyprpaper.conf` (`preload =` / `wallpaper =`)

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

### Method 1: inotifywait + exec-once

Add to `~/.config/hypr/hyprland.conf`:

```conf
exec-once = ~/Downloads/wap-kitty/hyprland-watcher.sh
```

Create `~/Downloads/wap-kitty/hyprland-watcher.sh`:

```bash
#!/bin/bash
while inotifywait -qe close_write "$HOME/.config/hypr/hyprpaper.conf"; do
  wap
done
```

```bash
chmod +x ~/Downloads/wap-kitty/hyprland-watcher.sh
```

### Method 2: systemd path unit

```bash
cp ~/Downloads/wap-kitty/systemd/* ~/.config/systemd/user/
# Edit wap-kitty.path — change path to hyprpaper.conf
systemctl --user daemon-reload
systemctl --user enable --now wap-kitty.path
```

### Method 3: wallpaper script hook

```bash
#!/bin/bash
hyprctl hyprpaper wallpaper "eDP-1,$1"
wap
```

## ✅ Verify

```bash
wap
```
