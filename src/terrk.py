import click
import json
from .create import create_workspace, create_project
from .apply import apply
from .utility import init, clean, which, switch, check_context, CONFIG_FILE_PATH
from pathlib import Path


from typing import Literal

def extract_context():
    config_file_path = Path(CONFIG_FILE_PATH)
    if config_file_path.exists():
        with open(config_file_path, 'r') as file:
            content = json.load(file)
            cur_ctx = content["current"]
            token = content['contexts'][cur_ctx]["api_token"]
            return cur_ctx, token
    return ""
  
    
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


@click.argument("name")
@click.option("-a", "--agent-id", type=str, help="The id of the agent pool to use if exec-mode is set to agent")
@click.option("-e", "--exec-mode", default="local", type=str, help="supported options; local, remote, agent. Defaults to local")
@click.option("-d", "--description", type=str, help="The workspace description")
@click.option("--terraform-version", type=str, help="The version of Terraform to use for this workspace")
@click.option("-p", "--project-id", type=str, help="ID of the project to deploy the workspace in. Defaults to the default project")
@click.command()
@click.pass_context
def workspace(ctx: click.Context, name, description, terraform_version, exec_mode, agent_id, project_id):
    '''Create Terraform cloud workspace'''
    check_context(ctx.obj)
    context = ''.join(ctx.obj.keys())
    token = ctx.obj[context]
    
    create_workspace(org=context,
                     name=name, 
                     token=token, 
                     exec_mode=exec_mode,
                     agent_id=agent_id, 
                     project_id=project_id, 
                     description=description,  
                     terraform_version=terraform_version)


@click.argument("name")
@click.option("-d", "--description", type=str)
@click.command()
@click.pass_context
def project(ctx: click.Context, name, description):
    '''Create Terraform cloud project'''
    
    check_context(ctx.obj)

    context = ''.join(ctx.obj.keys())
    token = ctx.obj[context]
    create_project(org=context, token=token, description=description, project_name=name)



@click.command()
def agent():
    pass

@click.group()
def create():
    """Create resource using command line args"""





create.add_command(workspace)
create.add_command(project)
create.add_command(agent)

cli.add_command(create)
cli.add_command(apply)
cli.add_command(init)
cli.add_command(clean)
cli.add_command(switch)
cli.add_command(which)