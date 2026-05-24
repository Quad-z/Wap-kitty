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

# 🌿 nitrogen + wap-kitty

Автоматически подбирает цвета Kitty под твои обои при использовании nitrogen.

## 🔍 Как wap находит обои

Читает `~/.config/nitrogen/bg-saved.cfg`, поле `file=`.

## 🚀 Запуск

```bash
wap
```

## ⚡ Авто-применение при смене обоев

Добавь `wap` в конец скрипта смены обоев:

```bash
#!/bin/bash
nitrogen --set-zoom-fill "$1"
wap
```

## ✅ Проверка

```bash
wap
```
