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
