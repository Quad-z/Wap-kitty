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
