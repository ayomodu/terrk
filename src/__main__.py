import click
import os
from src.create import create
from src.apply import apply
from src.list import list
from src.delete import delete
from src.config import config, init, which
import sys

from src.utils.utility import (check_context, update_config, 
                      update_context, check_config, 
                      clean_context, read_config, 
                      extract_context,  create_config,
                      get_context_detail, delete_context,
                      switch_context,list_contexts,
                      CONFIG_DIR, CONFIG_FILE_PATH)

#Command Groups

@click.group()
@click.version_option()
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