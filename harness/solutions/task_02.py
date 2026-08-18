from . import replace

EDIT_FILES = ["src/logsift/config.py"]
READ_FILES = ["src/logsift/config.py"]
KEYWORDS = "ConfigError load_config TOML"


def apply(subject):
    config = subject / "src/logsift/config.py"
    replace(
        config,
        'DEFAULTS = {"min_level": "INFO", "max_lines": 10000}',
        'DEFAULTS = {"min_level": "INFO", "max_lines": 10000}\n'
        "\n"
        "\n"
        "class ConfigError(Exception):\n"
        "    pass",
    )
    replace(
        config,
        "def _read_toml(path) -> dict:\n"
        '    with open(path, "rb") as f:\n'
        "        return tomllib.load(f)",
        "def _read_toml(path) -> dict:\n"
        "    try:\n"
        '        with open(path, "rb") as f:\n'
        "            return tomllib.load(f)\n"
        "    except tomllib.TOMLDecodeError as e:\n"
        '        raise ConfigError(f"invalid TOML in {path}: {e}") from e',
    )
