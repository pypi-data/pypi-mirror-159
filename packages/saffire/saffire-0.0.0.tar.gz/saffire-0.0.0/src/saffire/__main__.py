"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Saffire."""


if __name__ == "__main__":
    main(prog_name="saffire")  # pragma: no cover
