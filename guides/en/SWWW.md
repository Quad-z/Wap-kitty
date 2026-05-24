# 🌊 swww + wap-kitty

Automatically match your Kitty terminal colors when using swww.

## 🔍 Detection

Runs `swww query` and parses `image: "..."` from output.

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

Append `wap` to your wallpaper script:

```bash
#!/bin/bash
swww img "$1"
wap
```

## ✅ Verify

```bash
wap
```
