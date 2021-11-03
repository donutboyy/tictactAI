import click
from tictactai.output import start

@click.command()
@click.option('--pvp/--ai', default=False, help='Play vs a player or AI')
def cli(pvp):
    """Play a game of tic tac toe against an AI"""
    start(pvp)