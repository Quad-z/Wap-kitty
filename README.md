# 🐱 wap-kitty   UPDATE! (hyprland/kde/and more!)

<p align="center">
  <img src="photos/obzoor.gif" alt="wap-kitty Demo" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue.svg?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Terminal-Kitty-green.svg?style=flat-square" alt="Kitty">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License">
</p>

---

`wap-kitty` is a high-performance CLI automation utility written in Python that dynamically generates and applies harmonious, accessibility-first color schemes for the Kitty terminal based on your current desktop wallpaper. The project utilizes Google's advanced **Material 3 (M3) TonalSpot** quantization algorithm to mathematically calculate perfectly balanced color schemes.

Unlike traditional terminal theme generators (such as `pywal`) that blindly grab raw pixels or extract muddy, uncontrasted clusters, `wap-kitty` relies on the perceptual rigor of the **HCT (Hue, Chroma, Tone)** color space. Upon execution, it updates your configuration instantly and prints the active palette directly to `stdout` with clean, True Color terminal blocks.

---

## ✨ Key Features

<p align="center">
  <img src="photos/Untitled(1).png" alt="wap-kitty Palette Output" width="90%">
</p>

* 🧠 **M3 TonalSpot Engine:** Native generation of *Primary, Secondary, Tertiary, Neutral, and Error* palettes using Google's official C++ binaries compiled via `pybind11`.
* 👁️ **Contrast Enforcement:** Built-in compliance with perceptual readability standards (default contrast ratio of `3.0`) ensures your text never blends illegibly into the terminal background.
* 🎨 **Deep UI Theming:** Goes far beyond standard 16 ANSI overrides—it dynamically maps and themes your background, foreground, cursor, active text selections, window borders, and tab bars.
* ⚡ **Performance Optimized:** Wallpaper images are automatically downscaled to $128 \times 128$ before undergoing a hardware-accelerated k-means clustering process for instant execution.
* 🔄 **Zero-Click Automation:** Native systemd path units track live wallpaper modifications in `noctalia` on the fly, matching your terminal environment to your desktop without any user intervention.
* 🌐 **Cross-Platform Auto-Detection:** Automatically detects your current wallpaper on KDE, GNOME, Hyprland, Sway, XFCE, Cinnamon, MATE, macOS, Windows, and more.

---

## 📂 Project Architecture & File Tree

The project utilizes a modular Python design driven by a robust bash wrapper to eliminate system environment overhead:

```text
wap-kitty/
├── wap                  # Bash wrapper script (injects root into PYTHONPATH)
├── guides/              # Platform-specific setup guides (EN + RU)
│   ├── en/              # English guides
│   │   ├── NIRI.md
│   │   ├── HYPRLAND.md
│   │   ├── KDE.md
│   │   ├── GNOME.md
│   │   ├── SWAY.md
│   │   ├── XFCE.md
│   │   ├── CINNAMON.md
│   │   ├── MATE.md
│   │   ├── FEH.md
│   │   ├── NITROGEN.md
│   │   ├── SWWW.md
│   │   ├── MACOS.md
│   │   └── WINDOWS.md
│   └── ru/              # Russian guides
│       ├── NIRI.md
│       ├── HYPRLAND.md
│       ├── KDE.md
│       ├── GNOME.md
│       ├── SWAY.md
│       ├── XFCE.md
│       ├── CINNAMON.md
│       ├── MATE.md
│       ├── FEH.md
│       ├── NITROGEN.md
│       ├── SWWW.md
│       ├── MACOS.md
│       └── WINDOWS.md
├── install.sh           # Automated dependency installer & symlink manager
├── README.md            # Comprehensive project documentation
├── .gitignore           # Explicitly filters __pycache__/ and *.pyc
├── systemd/
│   ├── wap-kitty.path   # Systemd Path unit (monitors wallpapers.json changes)
│   └── wap-kitty.service# Systemd Service unit (triggers the generator execution)
└── wap_kitty/
    ├── __init__.py      # Version metadata (1.0.0), exports main entry
    ├── __main__.py      # Execution gateway for python -m wap_kitty
    └── core.py          # Core logic (Wallpaper detection, M3 processing, config engine — 157 lines)
```

---

## 🚀 Installation (one time, any OS)

```bash
# 1. Install M3 engine (Google Material Color Utilities)
pip install --user --break-system-packages material-color-utilities

# 2. Symlink the wap command
ln -sf ~/Downloads/wap-kitty/wap ~/.local/bin/wap

# 3. Verify PATH
echo $PATH  # should contain ~/.local/bin
```

### Check kitty.conf

Make sure `~/.config/kitty/kitty.conf` includes:

```conf
include current-theme.conf
```

Without this line, Kitty won't load the generated theme.

---

## 🎯 Basic Usage

```bash
# Auto-detect wallpaper → M3 palette → Kitty
wap

# Or specify an image manually
wap ~/Pictures/wallpaper.jpg
```

After `wap`:
- Colors apply to Kitty **instantly**
- Terminal prints the palette with true-color swatches
- Theme files: `~/.cache/wal/colors-kitty.conf` and `~/.config/kitty/current-theme.conf`

---
<p align="center">
  <img src="photos/Untitled(1).png" alt="wap-kitty Palette Output" width="90%">
</p>

## 🖥️ Platform Guides

| Platform | EN | RU |
|----------|----|-----|
| 🐱 **noćtalia (niri)** | [EN](guides/en/NIRI.md) | [RU](guides/ru/NIRI.md) |
| 🦎 **Hyprland** | [EN](guides/en/HYPRLAND.md) | [RU](guides/ru/HYPRLAND.md) |
| 🌀 **KDE Plasma** | [EN](guides/en/KDE.md) | [RU](guides/ru/KDE.md) |
| 🐚 **GNOME** | [EN](guides/en/GNOME.md) | [RU](guides/ru/GNOME.md) |
| 🗼 **Sway** | [EN](guides/en/SWAY.md) | [RU](guides/ru/SWAY.md) |
| 🐭 **XFCE** | [EN](guides/en/XFCE.md) | [RU](guides/ru/XFCE.md) |
| 🥮 **Cinnamon** | [EN](guides/en/CINNAMON.md) | [RU](guides/ru/CINNAMON.md) |
| 🧉 **MATE** | [EN](guides/en/MATE.md) | [RU](guides/ru/MATE.md) |
| 🖼️ **feh** | [EN](guides/en/FEH.md) | [RU](guides/ru/FEH.md) |
| 🌿 **nitrogen** | [EN](guides/en/NITROGEN.md) | [RU](guides/ru/NITROGEN.md) |
| 🌊 **swww** | [EN](guides/en/SWWW.md) | [RU](guides/ru/SWWW.md) |
| 🍎 **macOS** | [EN](guides/en/MACOS.md) | [RU](guides/ru/MACOS.md) |
| 🪟 **Windows** | [EN](guides/en/WINDOWS.md) | [RU](guides/ru/WINDOWS.md) |

---

## 🛠️ For Developers: How It Works

### 1. Wallpaper Detection (`detect_wallpaper()`)

Iterates detectors in priority order, returns the first valid path:

1. `_noctalia()` — JSON state file
2. `_kde()` — plasma config
3. `_hyprland()` — hyprctl or hyprpaper.conf
4. `_sway()` — swaymsg or process scan
5. `_gnome()` — gsettings
6. `_xfce()` — xfconf-query
7. `_cinnamon()` — gsettings
8. `_mate()` — gsettings
9. `_feh()` — ~/.fehbg
10. `_nitrogen()` — bg-saved.cfg
11. `_swww()` — swww query
12. `_macos()` — osascript
13. `_windows()` — PowerShell

### 2. M3 TonalSpot (`apply()`)

```python
img = Image.open(wallpaper)
theme = m3_theme_from_image(img, variant=Variant.TONALSPOT)
dark = theme.schemes.dark
```

- Resize to 128×128
- K-means color clustering (dominant color extraction)
- 5 TonalPalettes (primary, secondary, tertiary, neutral, error)
- Maps 16 ANSI colors + tab colors to specific tonal levels

**ANSI → M3 Tone Mapping:**

| kitty | Palette | Tone | Role |
|-------|---------|------|------|
| background | primary | 5 | Very dark background |
| foreground | neutral | 95 | Light text |
| color0 | neutral | 10 | Black |
| color1 | error | 60 | Red |
| color2 | secondary | 55 | Green |
| color3 | tertiary | 65 | Yellow |
| color4 | primary | 55 | Blue |
| color5 | tertiary | 65 | Magenta |
| color6 | secondary | 65 | Cyan |
| color7 | neutral | 92 | White |
| color8–15 | ... | ... | Light variants at +15–20 tone |

### 3. Output

- `~/.cache/wal/colors-kitty.conf` — pywal compatibility
- `~/.config/kitty/current-theme.conf` — primary theme
- stdout — palette preview with true-color blocks
