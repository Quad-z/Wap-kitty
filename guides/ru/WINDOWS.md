# 🪟 Windows + wap-kitty

Автоматически подбирает цвета Kitty под твои обои на Windows.

## 🔍 Как wap находит обои

Через PowerShell:
```powershell
Get-ItemProperty -Path 'HKCU:/Control Panel/Desktop' -Name Wallpaper
```

## 🚀 Запуск

```powershell
wap
```

## ⚡ Авто-применение при смене обоев

Через **Планировщик задач**:
- Триггер: при смене обоев
- Или запуск по расписанию (каждые N минут)

## ✅ Проверка

```powershell
wap
```
