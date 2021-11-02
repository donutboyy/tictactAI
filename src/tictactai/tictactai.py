import click
from .output import *

@click.command()
@click.option('--pvp', default=False, help='player vs player')
def begin(pvp):
    start()