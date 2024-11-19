from pythondaq.arduino_device import list_resources
import click

@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.option(
    "--list",
    help='.',
    show_default=True
)

def list():
    print(list_resources())