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

# 🌊 swww + wap-kitty

Автоматически подбирает цвета Kitty под твои обои при использовании swww.

## 🔍 Как wap находит обои

Выполняет `swww query` и парсит `image: "..."` из вывода.

## 🚀 Запуск

```bash
wap
```

## ⚡ Авто-применение при смене обоев

Добавь `wap` в конец скрипта смены обоев:

```bash
#!/bin/bash
swww img "$1"
wap
```

## ✅ Проверка

```bash
wap
```
