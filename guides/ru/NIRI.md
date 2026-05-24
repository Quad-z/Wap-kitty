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

# 🐱 noćtalia (niri) + wap-kitty

Автоматически подбирает цвета Kitty под твои обои на niri.

## 🔍 Как wap находит обои

Читает `~/.cache/noctalia/wallpapers.json`.

## 🚀 Запуск

```bash
wap
```

## ⚡ Авто-применение при смене обоев

Уже настроено через systemd:

```bash
systemctl --user status wall-theme.path
```

Если нужно включить вручную:

```bash
cp ~/Downloads/wap-kitty/systemd/* ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now wap-kitty.path
```

## ✅ Проверка

```bash
wap
```
