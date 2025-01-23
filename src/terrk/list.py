import click
from src.terrk.utils.utility import check_context, get_context_detail
from src.terrk.utils.list_core import list_projects, list_workspaces, list_agents, list_teams

@click.group()
def list():
    '''List Terraform cloud resources'''
    pass

@click.command()
@click.pass_context
@click.option("-n", "--number", type=int, help="Number of results to dispaly",show_default=True, default=20)
def projects(ctx: click.Context, number):
    '''List projects in Terraform cloud organization'''
    
    check_context(ctx.obj)
    org, token = get_context_detail(ctx.obj)
    list_projects(number=number, org=org, token=token)

@click.command()
@click.pass_context
@click.option("-n", "--number", type=int, help="Number of results to dispaly",show_default=True, default=20)
@click.option("-p", "--project-id", type=str, required=True, help="Project ID to filter results by")
def workspaces(ctx: click.Context, number, project_id):
    '''List workspaces in Terraform cloud organization'''
    
    check_context(ctx.obj)
    org, token = get_context_detail(ctx.obj)
    list_workspaces(number=number, project_id=project_id ,org=org, token=token)

@click.command()
@click.pass_context
@click.option("-n", "--number", type=int, help="Number of results to dispaly",show_default=True, default=10)
def agents(ctx: click.Context, number):
    '''List agent pools in Terraform cloud organization'''

    check_context(ctx.obj)
    org, token = get_context_detail(ctx.obj)
    list_agents(number=number,org=org, token=token)

@click.command()
@click.pass_context
@click.option("-n", "--number", type=int, help="Number of results to dispaly",show_default=True, default=10)
def teams(ctx: click.Context, number):
    '''List teams in Terraform cloud organization [beta(untested)]'''
    check_context(ctx.obj)
    org, token = get_context_detail(ctx.obj)
    list_teams(number=number,org=org, token=token)

list.add_command(projects)
list.add_command(workspaces)
list.add_command(agents)
list.add_command(teams)