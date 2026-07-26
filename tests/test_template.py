import subprocess
import tomllib
from pathlib import Path

REQUIRED_RUFF_SELECTORS = {
    "D",
    "DJ",
    "DTZ",
    "E",
    "F",
    "FBT",
    "FLY",
    "G",
    "INT",
    "LOG",
    "N",
    "PGH",
    "PTH",
    "PT",
    "PYI",
    "S",
    "TC",
    "YTT",
}


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, check=True, text=True, capture_output=True)


def test_template_generates_project(tmp_path):
    destination = tmp_path / "internal-app"

    run(
        [
            "uv",
            "run",
            "copier",
            "copy",
            "--trust",
            "--defaults",
            ".",
            str(destination),
        ],
        cwd=Path.cwd(),
    )

    assert (destination / "manage.py").exists()
    assert (destination / "internal_app" / "config" / "settings" / "base.py").exists()
    assert (destination / "internal_app" / "apps" / "core" / "admin.py").exists()


def test_generated_project_quality_checks(tmp_path):
    destination = tmp_path / "internal-app"
    run(
        [
            "uv",
            "run",
            "copier",
            "copy",
            "--trust",
            "--defaults",
            "--data",
            "create_demo_data=false",
            ".",
            str(destination),
        ],
        cwd=Path.cwd(),
    )

    run(["uv", "sync"], cwd=destination)
    run(["make", "qa"], cwd=destination)


def test_ruff_rules_match_the_base_template_standards():
    template_root = Path(__file__).resolve().parent.parent
    root_config = tomllib.loads((template_root / "pyproject.toml").read_text(encoding="utf-8"))
    assert set(root_config["tool"]["ruff"]["lint"]["select"]) >= REQUIRED_RUFF_SELECTORS

    generated_template = (template_root / "project/pyproject.toml.jinja").read_text(encoding="utf-8")
    for selector in REQUIRED_RUFF_SELECTORS:
        assert f'"{selector}"' in generated_template


def test_copier_uses_strict_templates_and_preserves_project_files():
    copier_config = (Path(__file__).resolve().parent.parent / "copier.yml").read_text(encoding="utf-8")

    assert "undefined: jinja2.StrictUndefined" in copier_config
    assert "_skip_if_exists:\n  - .python-version\n  - README.md" in copier_config
