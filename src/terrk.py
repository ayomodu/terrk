import click
import os
from .create import create
from .apply import apply
from .config import config, init, which
import sys

from .utils.utility import (check_context, update_config, 
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
