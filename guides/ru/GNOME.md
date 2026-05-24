# 🐚 GNOME + wap-kitty

Автоматически подбирает цвета Kitty под твои обои на GNOME.

## 🔍 Как wap находит обои

Через `gsettings`:
```bash
gsettings get org.gnome.desktop.background picture-uri-dark
```
Или fallback на `picture-uri`.

## 🚀 Запуск

```bash
wap
```

## ⚡ Авто-применение при смене обоев

Создай `~/Downloads/wap-kitty/gnome-watcher.sh`:

```bash
#!/bin/bash
while true; do
  gsettings monitor org.gnome.desktop.background picture-uri-dark | while read -r line; do
    wap
  done
done
```

```bash
chmod +x ~/Downloads/wap-kitty/gnome-watcher.sh
```

Добавь в автозапуск:
- Через `gnome-session-properties`
- Или положи `.desktop` файл в `~/.config/autostart/`

## ✅ Проверка

```bash
wap
```
