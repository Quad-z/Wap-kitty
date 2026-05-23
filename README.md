                # 🐱 wap-kitty

<img src="photos/Untitled(1).png" alt="wap-kitty Preview" width="100%">



Generate a **kitty terminal theme** from your wallpaper using **Material 3 (M3) TonalSpot** color extraction.

## Usage

```bash
# Auto-detect current wallpaper (noctalia)
wap

# Or pass an image directly
wap ~/Pictures/wallpaper.jpg
```

## Install

```bash
# 1. Install dependency
pip install --user --break-system-packages material-color-utilities

# 2. Symlink
ln -sf "$(pwd)/wap" ~/.local/bin/wap

# 3. (Optional) Auto-apply on wallpaper change
cp systemd/wap-kitty.{service,path} ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now wap-kitty.path
```
