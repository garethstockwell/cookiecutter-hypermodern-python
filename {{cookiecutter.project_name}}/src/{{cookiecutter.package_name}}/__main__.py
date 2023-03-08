"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """{{cookiecutter.friendly_name}}."""


def foo() -> str:
    """Return a string."""
    return "foo"


if __name__ == "__main__":
    main(prog_name="{{cookiecutter.project_name}}")  # pragma: no cover
