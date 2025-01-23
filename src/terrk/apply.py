import click
from src.terrk.utils.apply_core import validate_and_deploy_workspace
from src.terrk.utils.utility import check_context, get_context_detail

@click.group()
def apply():
    '''Create resource using a yaml or xlsx file'''
    pass

@click.option("-f", "--file", required=True, help="Specify the path to the (yaml|xlsx) config file", type=click.Path(exists=True))
@click.command()
@click.pass_context
def workspace(ctx: click.Context, file):
    check_context(ctx.obj)
    org, token = get_context_detail(ctx.obj)
    validate_and_deploy_workspace(file=file, org=org, token=token)



apply.add_command(workspace)
