import click
import os
from terrk.create import create
from terrk.apply import apply
from terrk.list import list
from terrk.delete import delete
from terrk.config import config, init, which
import sys

from terrk.utils.utility import ( 
                      extract_context
                      )


from importlib.metadata import version, PackageNotFoundError

try:
    package_version = version("terrk")
except PackageNotFoundError:
    sem_ver="0.1.2"
    package_version = sem_ver 

#Command Groups

@click.group()
@click.version_option(package_version, prog_name="terrk")
@click.pass_context
def cli(ctx: click.Context):
    ''' A tool to manage TFC resources'''
    if ctx.obj is None:
        ctx.obj = {}
        val = extract_context()
        if val:
            ctx.obj[val[0]] = val[1]
            return

#Context management commands



cli.add_command(create)
cli.add_command(apply)
cli.add_command(init)
cli.add_command(which)
cli.add_command(config)
cli.add_command(delete)
cli.add_command(list)

if __name__ == '__main__':
    cli()