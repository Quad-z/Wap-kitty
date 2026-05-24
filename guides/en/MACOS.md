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
