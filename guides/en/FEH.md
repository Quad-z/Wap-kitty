# 🖼️ feh + wap-kitty

Automatically match your Kitty terminal colors when using feh.

## 🔍 Detection

Parses `~/.fehbg` for arguments after `--bg-scale`/`--bg-fill`/`--bg-center`/`--bg-tile`.

## 🚀 Usage

```bash
wap
```

## ⚡ Auto-apply on wallpaper change

Append `wap` to your wallpaper script:

```bash
#!/bin/bash
feh --bg-scale "$1"
wap
```

## ✅ Verify

```bash
wap
```
