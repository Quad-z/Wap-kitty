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
