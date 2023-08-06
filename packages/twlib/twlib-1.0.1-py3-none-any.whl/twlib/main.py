import datetime
from pathlib import Path

import typer
from dateutil.parser import parse

app = typer.Typer(name="twlib")


@app.command()
def hello(
    name: str,
    create_png: bool = typer.Option(False, help="create a png."),
    file: Path = typer.Argument(default=None, help="ultisnips source", exists=True),
):
    typer.echo(f"Hello {name}, {file}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


@app.command()
def epoch2dt(
    epoch: int = typer.Argument(..., help="epoch in seconds"),
    to_local: bool = typer.Option(False, help="In local time"),
):
    if to_local:
        dt = datetime.datetime.fromtimestamp(epoch).strftime("%Y-%m-%d %H:%M:%S")
    else:
        dt = datetime.datetime.utcfromtimestamp(epoch).strftime("%Y-%m-%d %H:%M:%S")

    typer.echo(dt)


@app.command()
def dt2epoch(
    dt: str = typer.Argument(..., help="datetime string in '%Y-%m-%d %H:%M:%S'"),
    is_local: bool = typer.Option(False, help="Input is given in local time"),
):
    """Convert datetime string to epoch"""
    if is_local:
        # https://stackoverflow.com/a/39079819
        LOCAL_TIMEZONE = (
            datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        )

        dt_parsed = parse(dt)  # get naive dt
        dt_parsed = dt_parsed.replace(tzinfo=LOCAL_TIMEZONE)  # localize naive dt
    else:
        dt_parsed = parse(dt)
        dt_parsed = dt_parsed.replace(tzinfo=datetime.timezone.utc)

    epoch = dt_parsed.timestamp()

    typer.echo(epoch)


if __name__ == "__main__":
    app()
