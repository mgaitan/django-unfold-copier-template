import subprocess
from pathlib import Path


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
    run(["uv", "run", "python", "manage.py", "check"], cwd=destination)
    run(["uv", "run", "pytest", "-q"], cwd=destination)
