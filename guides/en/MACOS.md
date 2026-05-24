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

# 🍎 macOS + wap-kitty

Automatically match your Kitty terminal colors to your macOS wallpaper.

## 🔍 Detection

Runs `osascript -e 'tell app "System Events" to get picture of every desktop'`.

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

### Method 1: cron

```bash
*/5 * * * * $HOME/.local/bin/wap
```

### Method 2: wallpaper script hook

```bash
#!/bin/bash
osascript -e "tell app \"Finder\" to set desktop picture to POSIX file \"$1\""
wap
```

## ✅ Verify

```bash
wap
```
