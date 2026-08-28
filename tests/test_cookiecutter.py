import subprocess
from pathlib import Path

import pytest

# Keep in sync with the "project_name" default in cookiecutter.json
PROJECT_NAME = "hsf-training-my-module"

IGNORED = {".DS_Store", "__pycache__"}


def _num_items(directory: Path) -> int:
    return len([p for p in directory.iterdir() if p.name not in IGNORED])


@pytest.fixture(scope="module")
def baked(tmp_path_factory) -> Path:
    """Generate a module with the default values and return its path."""
    output_dir = tmp_path_factory.mktemp("baked")
    result = subprocess.run(
        ["cookiecutter", ".", "--no-input", "--output-dir", str(output_dir)],
    )
    assert result.returncode == 0
    return output_dir / PROJECT_NAME


def test_expected_layout(baked):
    assert (baked / "book" / "_config.yml").is_file()
    assert (baked / "book" / "_toc.yml").is_file()
    assert (baked / "book" / "hsf-logo.png").is_file()
    assert (baked / ".all-contributorsrc").is_file()
    assert (baked / ".github" / "workflows" / "deploy.yml").is_file()
    # Update these counts whenever files are added to or removed from the template
    assert _num_items(baked) == 13
    assert _num_items(baked / "book") == 8
    assert _num_items(baked / ".github") == 5
    assert _num_items(baked / ".github" / "workflows") == 3


def test_rendering(baked):
    config = (baked / "book" / "_config.yml").read_text()
    assert "Title of the training module" in config
    assert f"https://github.com/hsf-training/{PROJECT_NAME}" in config
    readme = (baked / "README.md").read_text()
    assert "ALL-CONTRIBUTORS-LIST:START" in readme
    assert PROJECT_NAME in readme
    contributorsrc = (baked / ".all-contributorsrc").read_text()
    assert f'"projectName": "{PROJECT_NAME}"' in contributorsrc


def test_no_leftover_jinja(baked):
    for path in baked.rglob("*"):
        if path.is_file() and path.suffix not in {".png", ".ipynb"}:
            assert "cookiecutter." not in path.read_text(errors="ignore"), path
