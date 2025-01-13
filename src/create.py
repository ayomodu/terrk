import click
from src.utils.utility import check_context, get_context_detail
from src.utils.create_core import (create_workspace, create_project, 
                                create_agent_and_token, create_agent_token,
                                create_team_and_token, create_team_token)

@click.group()
def create():
    """Create resources using command line args"""

#Resource management (Create commands)

@click.argument("name")
@click.option("-a", "--agent-id", type=str, help="The id of the agent pool to use if exec-mode is set to agent")
@click.option("-e", "--exec-mode", show_default=True, default="local", type=str, help="supported options; local, remote, agent.")
@click.option("-d", "--description", type=str, help="The workspace description")
@click.option("--terraform-version", type=str, help="The version of Terraform to use for this workspace [default: latest] ")
@click.option("-p", "--project-id", type=str, help="ID of the project to deploy the workspace in. [default: default project]")
@click.command()
@click.pass_context
def workspace(ctx: click.Context, name, description, terraform_version, exec_mode, agent_id, project_id):
    '''Create Terraform cloud workspace'''
    check_context(ctx.obj)
    org, token = get_context_detail(ctx.obj)
    
    create_workspace(org=org,
                     name=name, 
                     token=token, 
                     exec_mode=exec_mode,
                     agent_id=agent_id, 
                     project_id=project_id, 
                     description=description,  
                     terraform_version=terraform_version)


@click.argument("name")
@click.option("-d", "--description", type=str, help="Project description")
@click.command()
@click.pass_context
def project(ctx: click.Context, name, description):
    '''Create Terraform cloud project'''
    
    check_context(ctx.obj)
    org, token = get_context_detail(ctx.obj)
    create_project(org=org, token=token, description=description, project_name=name)



@click.command()
@click.argument("name", type=str)
@click.option("-d", "--description", type=str, help="Agent token description, must be set if -t flag is set")
@click.option("-t", "--gen-token", is_flag=True, show_default=True, default=False, help="if set will create and output agent token")
@click.pass_context
def agent(ctx: click.Context, name, description, gen_token):
    '''Create Terraform agent, agent-token and output token'''
    check_context(ctx.obj)

    org, token = get_context_detail(ctx.obj)
    create_agent_and_token(name=name, org=org, token=token, description=description, t=gen_token)


@click.command()
@click.option("-a", "--agent-id", required=True, type=str, help="Agent ID")
@click.option("-d", "--description", required=True, type=str, help="Agent token description, it must be set")
@click.pass_context
def agenttoken(ctx: click.Context, agent_id, description):
    '''Create Terraform agent-token and output token'''
    check_context(ctx.obj)
    org, token = get_context_detail(ctx.obj)
    create_agent_token(agent_id=agent_id, token=token, description=description)

@click.command()
@click.argument("name", type=str)
@click.option("-t", "--team-token", is_flag=True, help="if set will create and output team token")
@click.pass_context
def team(ctx: click.Context, name, team_token):
    '''Create Terraform cloud team [beta(untested)]'''
    check_context(ctx.obj)
    org, token = get_context_detail(ctx.obj)
    create_team_and_token(name=name, org=org, token=token, t=team_token)

@click.command()
@click.option("-t", "--team-id", required=True, help="Team id")
@click.option("-d", "--days", type=int, default=7, show_default=True ,help="Number of days the token will be valid for")
@click.pass_context
def teamtoken(ctx: click.Context, days, team_id):
    '''Create Terraform cloud team token [beta(untested)]'''
    check_context(ctx.obj)
    org, token = get_context_detail(ctx.obj)
    create_team_token(team_id=team_id, token=token, days=days)

create.add_command(workspace)
create.add_command(project)
create.add_command(agent)
create.add_command(agenttoken)
create.add_command(team)
create.add_command(teamtoken)