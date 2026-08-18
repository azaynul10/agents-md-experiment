import os
import tomllib
from pathlib import Path

DEFAULTS = {"min_level": "INFO", "max_lines": 10000}


def _read_toml(path) -> dict:
    with open(path, "rb") as f:
        return tomllib.load(f)


def load_config(cwd=None) -> dict:
    """Merge order: DEFAULTS, then ./logsift.toml, then file named by LOGSIFT_CONFIG."""
    cfg = dict(DEFAULTS)
    base = Path(cwd or os.getcwd()) / "logsift.toml"
    if base.exists():
        cfg.update(_read_toml(base))
    env_path = os.environ.get("LOGSIFT_CONFIG")
    if env_path and Path(env_path).exists():
        cfg.update(_read_toml(env_path))
    return cfg
