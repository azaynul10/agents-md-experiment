from logsift.config import load_config


def test_defaults(tmp_path, monkeypatch):
    monkeypatch.delenv("LOGSIFT_CONFIG", raising=False)
    cfg = load_config(cwd=tmp_path)
    assert cfg["min_level"] == "INFO"
    assert cfg["max_lines"] == 10000


def test_local_file_overrides_defaults(tmp_path, monkeypatch):
    monkeypatch.delenv("LOGSIFT_CONFIG", raising=False)
    (tmp_path / "logsift.toml").write_text('min_level = "ERROR"\n')
    cfg = load_config(cwd=tmp_path)
    assert cfg["min_level"] == "ERROR"


def test_env_file_overrides_local(tmp_path, monkeypatch):
    (tmp_path / "logsift.toml").write_text('min_level = "ERROR"\n')
    env_file = tmp_path / "env.toml"
    env_file.write_text('min_level = "DEBUG"\n')
    monkeypatch.setenv("LOGSIFT_CONFIG", str(env_file))
    cfg = load_config(cwd=tmp_path)
    assert cfg["min_level"] == "DEBUG"
