# 🐱 wap-kitty

<p align="center">
  <img src="photos/Untitled(1).png" alt="wap-kitty Preview" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python: 3.x">
  <img src="https://img.shields.io/badge/Terminal-Kitty-green.svg" alt="Terminal: Kitty">
</p>

Generate a beautiful, accessibility-first **Kitty terminal theme** from your wallpaper using the advanced **Material 3 (M3) TonalSpot** color extraction algorithm.

Unlike traditional generators (like `pywal`) that blindly grab raw pixels, `wap-kitty` utilizes color science and contrast-aware formulas to deliver perfectly legible terminal themes every single time.

---

## ✨ Features

* 🧪 **Material 3 TonalSpot:** Scientific calculation of Primary, Secondary, Tertiary, Neutral, and Error tones.
* 👁️ **Contrast Enforcement:** Built-in compliance with readability standards so your text never blends into the background.
* 🎨 **Full UI Theming:** Goes beyond ANSI colors to theme your background, foreground, cursor, selections, tab bars, and window borders.
* ⚡ **Seamless Automation:** Comes with an integrated systemd unit to update your terminal look instantly when your wallpaper changes.

---

## 💡 Usage

```bash
# Auto-detect current wallpaper (via noctalia wallpapers.json)
wap

# Or pass an image path directly for manual override
wap ~/Pictures/wallpaper.jpg
