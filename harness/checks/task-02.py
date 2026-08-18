import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import finish, suite_and_lint


def functional() -> bool:
    import os

    from logsift.config import ConfigError, load_config

    if not issubclass(ConfigError, Exception):
        print("FAIL: ConfigError is not an Exception subclass")
        return False

    with tempfile.TemporaryDirectory() as td:
        bad = Path(td) / "logsift.toml"
        bad.write_text("min_level = [broken\n")
        try:
            load_config(cwd=td)
            print("FAIL: no ConfigError for bad local file")
            return False
        except ConfigError as e:
            if "logsift.toml" not in str(e):
                print("FAIL: message lacks offending path:", e)
                return False

    with tempfile.TemporaryDirectory() as td:
        envf = Path(td) / "env.toml"
        envf.write_text("= nonsense =\n")
        os.environ["LOGSIFT_CONFIG"] = str(envf)
        try:
            load_config(cwd=td)
            print("FAIL: no ConfigError for bad env file")
            return False
        except ConfigError:
            pass
        finally:
            os.environ.pop("LOGSIFT_CONFIG", None)

    good = load_config(cwd=tempfile.gettempdir())
    if good.get("min_level") != "INFO":
        print("FAIL: defaults changed:", good)
        return False
    return True


if __name__ == "__main__":
    finish(suite_and_lint() and functional())
