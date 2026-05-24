# 🐭 XFCE + wap-kitty

Автоматически подбирает цвета Kitty под твои обои на XFCE.

## 🔍 Как wap находит обои

Через `xfconf-query -c xfce4-desktop -lv`, ищет ключи `last-image` или `image-path`.

## 🚀 Запуск

```bash
wap
```

## ⚡ Авто-применение при смене обоев

Создай `~/Downloads/wap-kitty/xfce-watcher.sh`:

```bash
#!/bin/bash
while inotifywait -qe close_write "$HOME/.config/xfce4/desktop/..." 2>/dev/null; do
  wap
done
```

```bash
chmod +x ~/Downloads/wap-kitty/xfce-watcher.sh
```

Добавь в автозапуск через **Session and Startup → Application Autostart**.

## ✅ Проверка

```bash
wap
```
