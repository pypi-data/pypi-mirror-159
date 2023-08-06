from subprocess import run


def test_help():
    """Test the cookiecutter-pypackage-test --help command."""
    run(["cookiecutter-pypackage-test", "--help"], check=True)


def test_version():
    """Test the cookiecutter-pypackage-test --version command."""
    run(["cookiecutter-pypackage-test", "--version"], check=True)
