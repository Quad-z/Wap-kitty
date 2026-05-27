import json
from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "wap-kitty"
SETTINGS_FILE = CONFIG_DIR / "settings.json"

DEFAULT = {
    "targets": {
        "kitty": True,
        "fastfetch": True,
    }
}


def load() -> dict:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if SETTINGS_FILE.exists():
        try:
            return {**DEFAULT, **json.loads(SETTINGS_FILE.read_text())}
        except Exception:
            pass
    SETTINGS_FILE.write_text(json.dumps(DEFAULT, indent=2) + "\n")
    return dict(DEFAULT)
