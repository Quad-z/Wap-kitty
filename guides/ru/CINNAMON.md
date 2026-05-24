# 🥮 Cinnamon + wap-kitty

Автоматически подбирает цвета Kitty под твои обои на Cinnamon.

## 🔍 Как wap находит обои

Через `gsettings get org.cinnamon.desktop.background picture-uri`.

## 🚀 Запуск

```bash
wap
```

## ⚡ Авто-применение при смене обоев

Создай `~/Downloads/wap-kitty/cinnamon-watcher.sh`:

```bash
#!/bin/bash
while true; do
  gsettings monitor org.cinnamon.desktop.background picture-uri | while read -r line; do
    wap
  done
done
```

```bash
chmod +x ~/Downloads/wap-kitty/cinnamon-watcher.sh
```

Добавь в автозапуск через **Preferences → Startup Applications**.

## ✅ Проверка

```bash
wap
```
