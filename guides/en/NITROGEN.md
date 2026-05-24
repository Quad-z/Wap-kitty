# 🌿 nitrogen + wap-kitty

Automatically match your Kitty terminal colors when using nitrogen.

## 🔍 Detection

Reads `~/.config/nitrogen/bg-saved.cfg`, field `file=`.

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

Append `wap` to your wallpaper script:

```bash
#!/bin/bash
nitrogen --set-zoom-fill "$1"
wap
```

## ✅ Verify

```bash
wap
```
