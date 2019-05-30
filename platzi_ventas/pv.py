import click

from clients import commands as clients_commands

CLIENTS_CSV = ".clients.csv"

@click.group()
@click.pass_context
def cli(ctx):
    """An application to manage clients, inventory, sales and produce reports."""
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_CSV


cli.add_command(clients_commands.all)
