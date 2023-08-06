import typer

from . import devices

app = typer.Typer()
app.add_typer(devices.app, name="devices")

if __name__ == "__main__":
    app()