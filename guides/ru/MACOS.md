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

# 🍎 macOS + wap-kitty

Автоматически подбирает цвета Kitty под твои обои на macOS.

## 🔍 Как wap находит обои

Через `osascript -e 'tell app "System Events" to get picture of every desktop'`.

## 🚀 Запуск

```bash
wap
```

## ⚡ Авто-применение при смене обоев

### Способ 1: cron

```bash
*/5 * * * * $HOME/.local/bin/wap
```

### Способ 2: хук в скрипт смены обоев

```bash
#!/bin/bash
osascript -e "tell app \"Finder\" to set desktop picture to POSIX file \"$1\""
wap
```

## ✅ Проверка

```bash
wap
```
