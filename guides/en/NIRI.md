# 🐱 noćtalia (niri) + wap-kitty

Automatically match your Kitty terminal colors to your niri wallpaper.

## 🔍 Detection

Reads `~/.cache/noctalia/wallpapers.json`.

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

Pre-configured via systemd:

```bash
systemctl --user status wall-theme.path
```

To enable manually:

```bash
cp ~/Downloads/wap-kitty/systemd/* ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now wap-kitty.path
```

## ✅ Verify

```bash
wap
```
