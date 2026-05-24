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
