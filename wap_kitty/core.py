import json
import os
import re
import subprocess
import sys
from pathlib import Path

from material_color_utilities import Variant
from material_color_utilities import theme_from_image as m3_theme_from_image
from PIL import Image

from . import settings

KITTY_DIR = Path.home() / ".config" / "kitty"
CACHE_DIR = Path.home() / ".cache" / "wal"
FASTFETCH_CONFIG = Path.home() / ".config" / "fastfetch" / "config.jsonc"


def detect_wallpaper() -> str | None:
    for method in DETECTORS:
        try:
            path = method()
            if path and Path(path).exists():
                return path
        except Exception:
            continue
    return None


def _noctalia() -> str | None:
    f = Path.home() / ".cache" / "noctalia" / "wallpapers.json"
    if not f.exists():
        return None
    data = json.loads(f.read_text())
    for mon in data.get("wallpapers", {}).values():
        p = mon.get("dark") or mon.get("light")
        if p:
            return p
    return None


def _kde() -> str | None:
    f = Path.home() / ".config" / "plasma-org.kde.plasma.desktop-appletsrc"
    if not f.exists():
        return None
    text = f.read_text()
    for m in re.finditer(r'^Image\s*=\s*(.+\.\w+)', text, re.M):
        return m.group(1).strip()
    for m in re.finditer(r'^wallpaper\w*\s*=\s*(.+\.\w+)', text, re.M):
        return m.group(1).strip()
    return None


def _gnome() -> str | None:
    for key in (
        "org.gnome.desktop.background picture-uri-dark",
        "org.gnome.desktop.background picture-uri",
    ):
        try:
            r = subprocess.run(
                ["gsettings", "get"] + key.split(),
                capture_output=True, text=True, timeout=3,
            )
            if r.returncode == 0:
                path = r.stdout.strip().strip("'")
                if path.startswith("file://"):
                    path = path[7:]
                if path:
                    return path
        except Exception:
            continue
    return None


def _hyprland() -> str | None:
    try:
        r = subprocess.run(
            ["hyprctl", "hyprpaper", "listloaded"],
            capture_output=True, text=True, timeout=3,
        )
        if r.returncode == 0:
            for line in r.stdout.strip().split("\n"):
                line = line.strip()
                if line:
                    return line
    except Exception:
        pass
    try:
        f = Path.home() / ".config" / "hypr" / "hyprpaper.conf"
        if f.exists():
            for line in f.read_text().split("\n"):
                line = line.strip()
                for prefix in ("preload =", "wallpaper ="):
                    if line.startswith(prefix):
                        parts = line.split("=", 1)
                        if len(parts) == 2:
                            path = parts[1].strip().split(",")[-1].strip()
                            if path:
                                return path
    except Exception:
        pass
    return None


def _sway() -> str | None:
    try:
        r = subprocess.run(
            ["swaymsg", "-t", "get_outputs"],
            capture_output=True, text=True, timeout=3,
        )
        if r.returncode == 0:
            data = json.loads(r.stdout)
            for out in data if isinstance(data, list) else [data]:
                cwp = out.get("current_wallpaper", "")
                if cwp:
                    return cwp
    except Exception:
        pass
    return _from_process("swaybg")


def _xfce() -> str | None:
    try:
        r = subprocess.run(
            ["xfconf-query", "-c", "xfce4-desktop", "-lv"],
            capture_output=True, text=True, timeout=3,
        )
        if r.returncode == 0:
            for line in r.stdout.strip().split("\n"):
                if "last-image" in line or "image-path" in line:
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        return parts[-1]
    except Exception:
        pass
    return None


def _cinnamon() -> str | None:
    try:
        r = subprocess.run(
            ["gsettings", "get", "org.cinnamon.desktop.background", "picture-uri"],
            capture_output=True, text=True, timeout=3,
        )
        if r.returncode == 0:
            path = r.stdout.strip().strip("'")
            if path.startswith("file://"):
                path = path[7:]
            if path:
                return path
    except Exception:
        pass
    return None


def _mate() -> str | None:
    try:
        r = subprocess.run(
            ["gsettings", "get", "org.mate.desktop.background", "picture-filename"],
            capture_output=True, text=True, timeout=3,
        )
        if r.returncode == 0:
            return r.stdout.strip().strip("'")
    except Exception:
        pass
    return None


def _feh() -> str | None:
    f = Path.home() / ".fehbg"
    if f.exists():
        for m in re.finditer(r'--bg\S*\s+[\'"]?(.+?)[\'"]?\s*$', f.read_text(), re.M):
            path = m.group(1).strip().strip("'\"")
            if path:
                return path
    return None


def _nitrogen() -> str | None:
    f = Path.home() / ".config" / "nitrogen" / "bg-saved.cfg"
    if f.exists():
        for line in f.read_text().split("\n"):
            if line.startswith("file="):
                return line.split("=", 1)[1].strip()
    return None


def _swww() -> str | None:
    try:
        r = subprocess.run(
            ["swww", "query"],
            capture_output=True, text=True, timeout=3,
        )
        if r.returncode == 0:
            for m in re.finditer(r'image:\s*"(.+?)"', r.stdout):
                return m.group(1)
    except Exception:
        pass
    return None


def _macos() -> str | None:
    try:
        r = subprocess.run(
            ["osascript", "-e",
             'tell app "System Events" to get picture of every desktop'],
            capture_output=True, text=True, timeout=3,
        )
        if r.returncode == 0:
            for line in r.stdout.strip().split(","):
                line = line.strip().strip(",").strip()
                if line:
                    return line
    except Exception:
        pass
    return None


def _from_process(name: str) -> str | None:
    try:
        r = subprocess.run(
            ["ps", "aux"],
            capture_output=True, text=True, timeout=3,
        )
        for line in r.stdout.split("\n"):
            if name in line:
                for m in re.finditer(r'[\'"]?([^\'"\s]+\.(?:png|jpg|jpeg|gif|bmp|webp))[\'"]?', line, re.I):
                    return m.group(1)
    except Exception:
        pass
    return None


def _windows() -> str | None:
    try:
        r = subprocess.run(
            ["powershell", "-Command",
             "Get-ItemProperty -Path 'HKCU:/Control Panel/Desktop' -Name Wallpaper | Select-Object -ExpandProperty Wallpaper"],
            capture_output=True, text=True, timeout=5,
        )
        if r.returncode == 0:
            return r.stdout.strip()
    except Exception:
        pass
    return None


DETECTORS = [
    _noctalia,
    _kde,
    _hyprland,
    _sway,
    _gnome,
    _xfce,
    _cinnamon,
    _mate,
    _feh,
    _nitrogen,
    _swww,
    _macos,
    _windows,
]


def make_kitty_conf(scheme, source_hex: str) -> str:
    pp = scheme.primary_palette
    sp = scheme.secondary_palette
    tp = scheme.tertiary_palette
    np = scheme.neutral_palette
    ep = scheme.error_palette

    def t(palette, tone):
        return palette.get_argb(tone) & 0xFFFFFF

    bg = t(pp, 5)
    fg = t(np, 95)
    cursor = t(pp, 80)
    cursor_text = t(pp, 5)
    sel_bg = t(pp, 40)
    sel_fg = t(np, 95)
    url_col = t(pp, 70)
    border_active = t(pp, 60)
    border_inactive = t(np, 25)

    c0 = t(np, 10)
    c1 = t(ep, 60)
    c2 = t(sp, 55)
    c3 = t(tp, 65)
    c4 = t(pp, 55)
    c5 = t(tp, 65)
    c6 = t(sp, 65)
    c7 = t(np, 92)
    c8 = t(np, 30)
    c9 = t(ep, 75)
    c10 = t(sp, 75)
    c11 = t(tp, 80)
    c12 = t(pp, 75)
    c13 = t(tp, 80)
    c14 = t(sp, 80)
    c15 = t(np, 97)

    lines = [
        f"## Generated by wap-kitty (M3 TonalSpot)",
        f"## Source color: {source_hex}",
        "",
        f"foreground         #{fg:06x}",
        f"background         #{bg:06x}",
        f"cursor             #{cursor:06x}",
        f"cursor_text_color  #{cursor_text:06x}",
        f"selection_foreground #{sel_fg:06x}",
        f"selection_background #{sel_bg:06x}",
        f"url_color          #{url_col:06x}",
        f"active_border_color   #{border_active:06x}",
        f"inactive_border_color #{border_inactive:06x}",
        "",
    ]

    for i, c in enumerate([c0, c1, c2, c3, c4, c5, c6, c7]):
        lines.append(f"color{i}       #{c:06x}")
    lines.append("")
    for i, c in enumerate([c8, c9, c10, c11, c12, c13, c14, c15]):
        lines.append(f"color{i + 8}       #{c:06x}")
    lines.append("")

    lines += [
        f"active_tab_foreground     #{bg:06x}",
        f"active_tab_background     #{t(pp, 60):06x}",
        f"inactive_tab_foreground   #{t(np, 80):06x}",
        f"inactive_tab_background   #{t(np, 15):06x}",
    ]

    return "\n".join(lines) + "\n"


def make_fastfetch_conf(dark) -> str | None:
    path = FASTFETCH_CONFIG
    if not path.exists():
        return None

    text = path.read_text()
    if text.startswith("{"):
        config = json.loads(text)

        def p(palette, tone):
            return f"#{palette.get_argb(tone) & 0xFFFFFF:06x}"

        pp = dark.primary_palette
        sp = dark.secondary_palette
        tp = dark.tertiary_palette
        np = dark.neutral_palette

        if "logo" in config and "color" in config["logo"]:
            config["logo"]["color"]["1"] = p(pp, 60)
            config["logo"]["color"]["2"] = p(sp, 55)
            config["logo"]["color"]["3"] = p(np, 90)

        for module in config.get("modules", []):
            if isinstance(module, dict) and "keyColor" in module:
                t = module.get("type", "")
                if t in ("os", "kernel", "uptime", "packages", "shell"):
                    module["keyColor"] = p(pp, 60)
                elif t in ("wm", "terminal", "theme", "icons", "cursor"):
                    module["keyColor"] = p(sp, 55)
                elif t in ("cpu", "gpu", "memory", "disk"):
                    module["keyColor"] = p(tp, 65)
                elif t == "colors":
                    module["keyColor"] = p(np, 40)
                elif t == "title":
                    module["keyColor"] = p(pp, 60)
                    if "color" in module:
                        module["color"]["user"] = p(pp, 60)
                        module["color"]["at"] = p(np, 80)
                        module["color"]["host"] = p(pp, 60)

        return json.dumps(config, indent=4)

    return None


def apply(wallpaper: str) -> None:
    cfg = settings.load()
    targets = cfg.get("targets", {})
    img = Image.open(wallpaper)
    theme = m3_theme_from_image(img, variant=Variant.TONALSPOT)
    dark = theme.schemes.dark

    source_hex = theme.source
    theme_content = make_kitty_conf(dark, source_hex)

    if targets.get("kitty", True):
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        (CACHE_DIR / "colors-kitty.conf").write_text(theme_content)

        KITTY_DIR.mkdir(parents=True, exist_ok=True)
        (KITTY_DIR / "current-theme.conf").write_text(theme_content)

    if targets.get("fastfetch", True):
        ff = make_fastfetch_conf(dark)
        if ff:
            FASTFETCH_CONFIG.parent.mkdir(parents=True, exist_ok=True)
            FASTFETCH_CONFIG.write_text(ff + "\n")

    def c(palette, tone):
        return palette.get_argb(tone) & 0xFFFFFF

    def block(hex_color: int) -> str:
        r = (hex_color >> 16) & 0xFF
        g = (hex_color >> 8) & 0xFF
        b = hex_color & 0xFF
        return f"\033[48;2;{r};{g};{b}m  \033[0m"

    pp = dark.primary_palette
    tp = dark.tertiary_palette
    np = dark.neutral_palette

    primary = c(pp, 55)
    secondary = c(dark.secondary_palette, 55)
    tertiary = c(tp, 65)
    fg = c(np, 95)
    bg = c(np, 10)

    print(f"  Wallpaper: {wallpaper}")
    print(f"  Source:    {source_hex}")
    print(f"  {block(primary)} Primary   #{primary:06x}")
    print(f"  {block(secondary)} Secondary #{secondary:06x}")
    print(f"  {block(tertiary)} Tertiary  #{tertiary:06x}")
    print(f"  {block(fg)} Foreground #{fg:06x}")
    print(f"  {block(bg)} Background #{bg:06x}")

    if targets.get("kitty", True):
        print(f"  {block(secondary)} Kitty theme written")
    if targets.get("fastfetch", True):
        print(f"  {block(primary)} Fastfetch (logo + key colors)")
    print()


def main() -> None:
    wallpaper = sys.argv[1] if len(sys.argv) > 1 else detect_wallpaper()

    if not wallpaper:
        print("Usage: wap [image]")
        print("  Without args - auto-detects wallpaper from your DE/WM")
        print("  Supported: KDE, GNOME, Hyprland, Sway, XFCE, Cinnamon,")
        print("             MATE, noćtalia, feh, nitrogen, swww, macOS, Windows")
        sys.exit(1)

    if not os.path.isfile(wallpaper):
        print(f"File not found: {wallpaper}")
        sys.exit(1)

    apply(wallpaper)
    print("Done")
