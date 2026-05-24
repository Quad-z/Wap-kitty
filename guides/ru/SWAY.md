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

# 🗼 Sway + wap-kitty

Автоматически подбирает цвета Kitty под твои обои на Sway.

## 🔍 Как wap находит обои

1. Пытается через `swaymsg -t get_outputs` (поле `current_wallpaper`)
2. Если не вышло — ищет `swaybg` в процессах и парсит аргументы

## 🚀 Запуск

```bash
wap
```

## ⚡ Авто-применение при смене обоев

### Способ 1: хук в скрипт запуска swaybg

```bash
#!/bin/bash
swaybg -i "$1" -m fill &
wap
```

### Способ 2: таймер в конфиге Sway

Добавь в `~/.config/sway/config`:

```
exec_always --no-startup-id while true; do sleep 30; wap; done
```

## ✅ Проверка

```bash
wap
```
