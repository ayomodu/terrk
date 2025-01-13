import click
from .utils.utility import check_context, get_context_detail, check_options
from .utils.delete_core import delete_workspace, delete_workspace_file, delete_project, delete_team, delete_agent

@click.group()
def delete():
    '''Delete TFC resources'''
    pass

@click.option("-n", "--name", type=str, help="Name of the workspace to delete")
@click.option("-f", "--file", type=str, help="Config file with list of workspaces to delete")
@click.command()
@click.pass_context
def workspace(ctx: click.Context, name, file):
    '''Delete Terraform cloud workspace/workspaces'''
    check_options(name=name, file=file)
    check_context(ctx.obj)
    org, token = get_context_detail(ctx.obj)
    if name:
        delete_workspace(org=org, token=token, name=name)
    if file:
        delete_workspace_file(org=org, token=token, file=file)

@click.command()
@click.pass_context
@click.argument("project_id", type=str)
def project(ctx: click.Context, project_id):
    '''Delete Terraform cloud project'''
    check_context(ctx.obj)
    org, token = get_context_detail(ctx.obj)
    delete_project(project_id=project_id, token=token)

@click.command()
@click.pass_context
@click.argument("team_id", type=str)
def team(ctx: click.Context, team_id):
    '''Delete Terraform cloud team [beta(untested)]'''
    check_context(ctx.obj)
    org, token = get_context_detail(ctx.obj)
    delete_team(team_id=team_id, token=token)

@click.command()
@click.pass_context
@click.argument("agent_pool_id", type=str)
def agent(ctx: click.Context, agent_pool_id):
    '''Delete Terraform cloud agent pool'''
    check_context(ctx.obj)
    org, token = get_context_detail(ctx.obj)
    delete_agent(agent_pool_id=agent_pool_id, token=token)

delete.add_command(workspace)
delete.add_command(project)
delete.add_command(team)
delete.add_command(agent)