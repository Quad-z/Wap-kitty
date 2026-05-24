# 🧉 MATE + wap-kitty

Автоматически подбирает цвета Kitty под твои обои на MATE.

## 🔍 Как wap находит обои

Через `gsettings get org.mate.desktop.background picture-filename`.

## 🚀 Запуск

```bash
wap
```

## ⚡ Авто-применение при смене обоев

Создай `~/Downloads/wap-kitty/mate-watcher.sh`:

```bash
#!/bin/bash
while true; do
  gsettings monitor org.mate.desktop.background picture-filename | while read -r line; do
    wap
  done
done
```

```bash
chmod +x ~/Downloads/wap-kitty/mate-watcher.sh
```

Добавь в автозапуск через **System → Preferences → Startup Applications**.

## ✅ Проверка

```bash
wap
```
