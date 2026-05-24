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
