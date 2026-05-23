# 🐱 wap-kitty

<p align="center">
  <img src="photos/Untitled(1).png" alt="wap-kitty Preview" width="100%">
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

* 🧠 **M3 TonalSpot Engine:** Native generation of *Primary, Secondary, Tertiary, Neutral, and Error* palettes using Google's official C++ binaries compiled via `pybind11`.
* 👁️ **Contrast Enforcement:** Built-in compliance with perceptual readability standards (default contrast ratio of `3.0`) ensures your text never blends illegibly into the terminal background.
* 🎨 **Deep UI Theming:** Goes far beyond standard 16 ANSI overrides—it dynamically maps and themes your background, foreground, cursor, active text selections, window borders, and tab bars.
* ⚡ **Performance Optimized:** Wallpaper images are automatically downscaled to $128 \times 128$ before undergoing a hardware-accelerated k-means clustering process for instant execution.
* 🔄 **Zero-Click Automation:** Native systemd path units track live wallpaper modifications in `noctalia` on the fly, matching your terminal environment to your desktop without any user intervention.

---

## 📂 Project Architecture & File Tree

The project utilizes a modular Python design driven by a robust bash wrapper to eliminate system environment overhead:

```text
wap-kitty/
├── wap                  # Bash wrapper script (injects root into PYTHONPATH)
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

### The Binary Wrapper (`wap`)

To ensure the modular `wap_kitty` package can be reliably executed from any working directory, the `wap` script handles paths deterministically:

```bash
#!/usr/bin/env bash
dir="$(cd "$(dirname "$(readlink -f "$0")")" && pwd)"
exec env PYTHONPATH="$dir${PYTHONPATH:+:$PYTHONPATH}" python3 -m wap_kitty "$@"

```

---

## 🛠 Installation & Setup

### 1. Clone the Repository

```bash
git clone [https://github.com/Quad-z/Wap-kitty.git](https://github.com/Quad-z/Wap-kitty.git)
cd Wap-kitty

```

### 2. Install Dependencies & Symlink

You can use the provided `install.sh` script or execute the setup steps manually:

```bash
# Install core required dependencies safely
pip install --user --break-system-packages material-color-utilities Pillow

# Create a symlink to easily run wap globally from your user path
ln -sf "$(pwd)/wap" ~/.local/bin/wap

```

### 3. Configure Kitty for Dynamic Loading

To let Kitty consume theme updates dynamically on the fly, append this single line to your `~/.config/kitty/kitty.conf`:

```kitty
include current-theme.conf

```

> ⚠️ **Note:** Your personal configuration values like `background_opacity` and `background_blur` are safely preserved and will not be overwritten by `wap-kitty`.

### 4. Enable Automated Hooks (Optional)

If you manage your desktop wallpapers using `noctalia`, seamlessly activate real-time background tracking:

```bash
cp systemd/wap-kitty.{service,path} ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now wap-kitty.path

```

---

## 💡 Usage

The command-line interface is built to be clean, intuitive, and minimal:

```bash
# Auto-detect current desktop wallpaper from ~/.cache/noctalia/wallpapers.json
wap

# Force-generate a theme layout from a specific image file path
wap ~/Pictures/my_wallpaper.jpg

# Quick test run using assets inside the repository
wap ~/Downloads/wap-kitty/photos/example.png

```

---

## ⚙️ Technical Specifications & Core Logic

### 1. Wallpaper Detection Pipeline

When run in auto-detect mode, `core.py` reads the active `~/.cache/noctalia/wallpapers.json` tracking file:

```json
{
  "wallpapers": {
    "HDMI-A-1": {
      "dark": "/home/user/wallpapers/image.png",
      "light": "/home/user/wallpapers/image.png"
    }
  }
}

```

The script safely parses the JSON, isolates the primary active monitor, grabs its `dark` (or `light`) path target, verifies the target file physically exists on your drive, and feeds it into the pipeline.

### 2. Material 3 → Kitty Mapping Matrix

Every generated `TonalPalette` exposes a native `get_argb(tone)` method where `tone` ranges from 0 to 100 (0 = Pure Black, 100 = Pure White). The core script masks out the alpha channels (`& 0xFFFFFF`) and strictly routes M3 architectural roles directly into Kitty configurations using this mapping matrix:

| Kitty Token | M3 Palette Source | Kitty Token | M3 Palette Source |
| --- | --- | --- | --- |
| **background** | `primary` | **color0 / color8** | `neutral` |
| **foreground** | `neutral` | **color1 / color9** | `error` |
| **cursor / text** | `primary` / `primary` | **color2 / color10** | `secondary` |
| **selection (bg/fg)** | `primary` / `neutral` | **color3 / color11** | `tertiary` |
| **url_color** | `primary` | **color4 / color12** | `primary` |
| **active_border** | `primary` | **color5 / color13** | `tertiary` |
| **inactive_border** | `neutral` | **color6 / color14** | `secondary` |
| **active_tab (fg/bg)** | `background` / `primary` | **color7 / color15** | `neutral` |
| **inactive_tab (fg/bg)** | `neutral` / `neutral` |  |  |

### 3. TonalSpot Quantization Engineering

Under the hood, `material-color-utilities` calculates a precise `Variant.TONALSPOT` scheme profile:

* **Chroma Constraints:** Primary = 36, Secondary = 16, Tertiary = 24, Neutral = 6, Neutral Variant = 8.
* **Hue Offsets:** Secondary tracks the seed hue exactly, Tertiary = Hue + 60°, Error = 25°.
* **Dual-Destination Export:** Output is simultaneously dumped to `~/.config/kitty/current-theme.conf` for direct Kitty consumption and written to `~/.cache/wal/colors-kitty.conf` to guarantee backward compatibility with traditional `pywal` pipelines.

---

## 📄 License

This project is open-source and released under the **MIT License**. See the `LICENSE` file for details.

```

```
