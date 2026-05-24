# 🦎 Hyprland + wap-kitty

Автоматически подбирает цвета Kitty под твои обои на Hyprland.

## 🔍 Как wap находит обои

1. Пытается выполнить `hyprctl hyprpaper listloaded`
2. Если не вышло — парсит `~/.config/hypr/hyprpaper.conf` (ищет `preload =` и `wallpaper =`)

## 🚀 Запуск

```bash
wap
```

## ⚡ Авто-применение при смене обоев

### Способ 1: inotifywait + exec-once

Добавь в `~/.config/hypr/hyprland.conf`:

```conf
exec-once = ~/Downloads/wap-kitty/hyprland-watcher.sh
```

Создай `~/Downloads/wap-kitty/hyprland-watcher.sh`:

```bash
#!/bin/bash
while inotifywait -qe close_write "$HOME/.config/hypr/hyprpaper.conf"; do
  wap
done
```

```bash
chmod +x ~/Downloads/wap-kitty/hyprland-watcher.sh
```

### Способ 2: systemd

```bash
cp ~/Downloads/wap-kitty/systemd/* ~/.config/systemd/user/
# Отредактируй wap-kitty.path — замени путь на hyprpaper.conf
systemctl --user daemon-reload
systemctl --user enable --now wap-kitty.path
```

### Способ 3: хук в скрипт смены обоев

```bash
#!/bin/bash
hyprctl hyprpaper wallpaper "eDP-1,$1"
wap
```

## ✅ Проверка

```bash
wap
```
