import click
import os
from .utils import utility

@click.group()
def config():
    '''Manage context configuration'''

@click.argument("org", type=str)
@click.option("-t","--token", prompt="Enter your TFC api Token", hide_input=True, type=str)
@click.command()
@click.pass_context
def init(ctx: click.Context, org, token):

    '''Initialize the configuration needed to work with TFC'''

    ctx.obj = { }

    #check if config file exists; if not; create TFC context 
    if not utility.check_config():
        click.echo(f"terrk Config file not found...Creating new...\n")
        try:
            os.mkdir(utility.CONFIG_DIR)
        except:
            pass
        finally:
            utility.create_config(org=org, token=token)
            utility.update_context(org)
            click.echo(f"terrk initialized!!! {org} context created at: {utility.CONFIG_FILE_PATH}")
        return
    
    #update the TFC config if file exists and contains context
    utility.update_config(org=org, token=token)
    utility.update_context(org)

    click.echo(f"terrk initialized!!! {org} context updated")
    return


@click.command()
@click.pass_context
def which(ctx: click.Context):
    '''Show the current context'''
    utility.check_context(ctx.obj)
    ctx_val = ''.join(ctx.obj.keys())
    click.echo(f"Current context: {ctx_val}")
    return
    

@click.command()
@click.pass_context   
def clean(ctx: click.Context):
    '''Remove all contexts - deletes the config file'''
    if click.confirm(f"Are you sure you want to delete the terrk config? this action is irreversible", abort=True):
        utility.clean_context(ctx.obj)
    

@click.command()
@click.argument("name", type=str)
def switch(name):
    '''Switch to alternate context'''
    utility.switch_context(name=name)

@click.argument("name", type=str)
@click.command()
@click.pass_context
def rmcontext(ctx: click.Context, name):
    '''Remove a context from config file'''
    utility.delete_context(name=name, context_obj=ctx.obj)


@click.command()
def lscontext():
    '''List all available contexts in config file'''
    utility.list_contexts()


config.add_command(clean)
config.add_command(switch)
config.add_command(lscontext)
config.add_command(rmcontext)
