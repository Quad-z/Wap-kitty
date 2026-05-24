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

# 🌀 KDE Plasma + wap-kitty

Автоматически подбирает цвета Kitty под твои обои на KDE.

## 🔍 Как wap находит обои

Читает `~/.config/plasma-org.kde.plasma.desktop-appletsrc` — находит строку `Image=/путь/к/обоям`.

## 🚀 Запуск

```bash
wap
```

## ⚡ Авто-применение при смене обоев

### Способ: скрипт в автозапуск KDE

1. Открой **System Settings → Автозапуск**
2. Нажми **Добавить → Локальный скрипт**
3. Укажи путь к `~/Downloads/wap-kitty/kde-watcher.sh`

Создай `~/Downloads/wap-kitty/kde-watcher.sh`:

```bash
#!/bin/bash
while inotifywait -qe close_write "$HOME/.config/plasma-org.kde.plasma.desktop-appletsrc"; do
  wap
done
```

```bash
chmod +x ~/Downloads/wap-kitty/kde-watcher.sh
```

## ✅ Проверка

```bash
wap
```
