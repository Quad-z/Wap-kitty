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
