import click
import requests
from .utility import set_token, check_response, get_workspace_config, validate_config
from .constants import WORKSPACE_DELETE_SCHEMA_EXCEL, WORKSPACE_DELETE_SCHEMA_YAML

def delete_workspace(name, org, token):
    headers = set_token(token)
    url = f"https://app.terraform.io/api/v2/organizations/{org}/workspaces/{name}"

    response = requests.delete(url=url, headers=headers)
    check_response(response=response, resource="Workspace")
    click.echo(f"Workspace {name} successfully deleted")

def delete_workspace_excel_file(workspace_config, org, token):
    for config in workspace_config:
        validate_config(config=config, schema=WORKSPACE_DELETE_SCHEMA_EXCEL)
        delete_workspace(name=config["WorkspaceName"], org=org, token=token)

def delete_workspace_yaml_file(workspace_config, org, token):
    for config in workspace_config:
        validate_config(config=config, schema=WORKSPACE_DELETE_SCHEMA_YAML)
        delete_workspace(name=config["resource"]["name"], org=org, token=token)

def delete_workspace_file(file, org, token):
    workspace_config, file_ext = get_workspace_config(file=file)
    if file_ext == ".xlsx":
        delete_workspace_excel_file(workspace_config, org=org, token=token)
        return
    if file_ext == ".yaml" or ".yml":
        delete_workspace_yaml_file(workspace_config, org, token)
        return

def delete_project(project_id, token):
    headers = headers = set_token(token)
    url = f"https://app.terraform.io/api/v2/projects/{project_id}"

    response =  requests.delete(url=url, headers=headers)
    check_response(response=response, resource="Project") 
    click.echo("Project successfully deleted")

def delete_team(team_id, token):
    headers = headers = set_token(token)
    url = f"https://app.terraform.io/api/v2/teams/{team_id}"
    response =  requests.delete(url=url, headers=headers)
    check_response(response=response, resource="Team") 
    click.echo("Team successfully deleted")

def delete_agent(agent_pool_id, token):
    headers = headers = set_token(token)
    url = f"https://app.terraform.io/api/v2/agent-pools/{agent_pool_id}"
    response =  requests.delete(url=url, headers=headers)
    check_response(response=response, resource="Agent Pool") 
    click.echo("Agent pool successfully deleted")