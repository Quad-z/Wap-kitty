## 🚀 Установка

Перед использованием установи зависимости и создай симлинк:

```bash
# Установка M3 движка (Google Material Color Utilities)
pip install --user --break-system-packages material-color-utilities

# Создание симлинка для команды wap
ln -sf ~/Downloads/wap-kitty/wap ~/.local/bin/wap

# Проверка PATH
echo $PATH  # должен содержать ~/.local/bin
```

### Проверка kitty.conf

Убедись, что в `~/.config/kitty/kitty.conf` есть строка:

```conf
include current-theme.conf
```

Без неё Kitty не увидит тему.

---

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
