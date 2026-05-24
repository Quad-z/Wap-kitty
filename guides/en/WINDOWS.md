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

# 🪟 Windows + wap-kitty

Automatically match your Kitty terminal colors to your Windows wallpaper.

## 🔍 Detection

Reads registry via PowerShell:
```powershell
Get-ItemProperty -Path 'HKCU:/Control Panel/Desktop' -Name Wallpaper
```

## 🚀 Usage

```powershell
wap
```

## ⚡ Auto-apply on wallpaper change

Use **Task Scheduler**:
- Trigger: on wallpaper change
- Or run on a schedule (every N minutes)

## ✅ Verify

```powershell
wap
```
