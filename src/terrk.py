import click
import os
from .create import create_workspace, create_project, create_agent_and_token, create_agent_token
from .apply import apply
import sys

from .utility import (check_context, update_config, 
                      update_context, check_config, 
                      clean_context, read_config, 
                      extract_context,  create_config,
                      get_context_detail, delete_context,
                      switch_context,
                      CONFIG_DIR, CONFIG_FILE_PATH)
    
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
    ctx_details = get_context_detail(ctx.obj)
    
    create_workspace(org=ctx_details[0],
                     name=name, 
                     token=ctx_details[1], 
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

    ctx_details = get_context_detail(ctx.obj)
    create_project(org=ctx_details[0], token=ctx_details[1], description=description, project_name=name)



@click.command()
@click.argument("name", type=str)
@click.option("-d", "--description", type=str, help="Agent token description, must be set if -t flag is set")
@click.option("-t", "--gen-token", is_flag=True, show_default=True, default=False, help="if set will create and output agent token")
@click.pass_context
def agent(ctx: click.Context, name, description, gen_token):
    '''Create Terraform agent, agent-token and output token'''
    check_context(ctx.obj)

    ctx_details = get_context_detail(ctx.obj)
    create_agent_and_token(name=name, org=ctx_details[0], token=ctx_details[1], description=description, t=gen_token)


@click.command()
@click.option("-a", "--agent-id", required=True, type=str, help="Agent ID")
@click.option("-d", "--description", required=True, type=str, help="Agent token description, it must be set")
@click.pass_context
def agenttoken(ctx: click.Context, agent_id, description):
    '''Create Terraform agent-token and output token'''
    check_context(ctx.obj)
    ctx_details = get_context_detail(ctx.obj)
    create_agent_token(agent_id=agent_id, token=ctx_details[1], description=description)



@click.group()
def create():
    """Create resource using command line args"""


#Context management commands

@click.argument("org", type=str)
@click.option("-t","--token", prompt="Enter your TFC api Token", hide_input=True, type=str)
@click.command()
@click.pass_context
def init(ctx: click.Context, org, token):

    '''Initialize the configuration needed to work with TFC'''

    ctx.obj = { }

    #check if config file exists; if not; create TFC context 
    if not check_config():
        click.echo(f"terrk Config file not found...Creating new...\n")
        try:
            os.mkdir(CONFIG_DIR)
        except:
            pass
        finally:
            create_config(org=org, token=token)
            update_context(org)
            click.echo(f"terrk initialized!!! {org} context created at: {CONFIG_FILE_PATH}")
        return
    
    #update the TFC config if file exists and contains context
    update_config(org=org, token=token)
    update_context(org)

    click.echo(f"terrk initialized!!! {org} context updated")
    return


@click.command()
@click.pass_context
def which(ctx: click.Context):
    '''Show the current context'''
    check_context(ctx.obj)
    ctx_val = ''.join(ctx.obj.keys())
    click.echo(f"Current context: {ctx_val}")
    return
    

@click.command()
@click.pass_context   
def clean(ctx: click.Context):
    '''Remove all contexts - deletes the config file'''
    clean_context(ctx.obj)
    

@click.command()
@click.argument("name", type=str)
def switch(name):
    '''Switch to alternate context'''
    switch_context(name=name)

@click.argument("name", type=str)
@click.command()
@click.pass_context
def rmcontext(ctx: click.Context, name):
    '''Remove a context from config file'''
    delete_context(name=name, context_obj=ctx.obj)


create.add_command(workspace)
create.add_command(project)
create.add_command(agent)
create.add_command(agenttoken)

cli.add_command(create)
cli.add_command(apply)
cli.add_command(init)
cli.add_command(clean)
cli.add_command(switch)
cli.add_command(which)
cli.add_command(rmcontext)