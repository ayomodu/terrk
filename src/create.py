import requests
import click
import json
import sys

from typing import Literal, Optional

from .constants import (PROJ_DATA, WORKSPACE_DATA,
                        WORKSPACE_PROJECT_REL,
                        HTTP_SUCCESS_CODES, AGENT_POOL_DATA,
                        AGENT_TOKEN_DATA)

from .utility import set_token, check_response


def create_workspace(project_id: str,
                     name: str, 
                     agent_id: Optional[str], 
                     token: str, 
                     description: Optional[str],
                     org: str,
                     exec_mode: Literal["local", "remote", "agent" ],
                     terraform_version = Optional[str]
                    ):
    click.echo(f"Attempting to create workspace {name}...\n")

    WORKSPACE_DATA["data"]["attributes"]["description"] = description
    WORKSPACE_DATA["data"]["attributes"]["execution-mode"] = exec_mode
    WORKSPACE_DATA["data"]["attributes"]["name"] = name

    if exec_mode == "agent":
        WORKSPACE_DATA["data"]["attributes"]["agent-pool-id"] = agent_id

    if terraform_version:
        WORKSPACE_DATA["data"]["attributes"]["terraform-version"] = terraform_version

    if project_id:
        WORKSPACE_PROJECT_REL["project"]["data"]["id"] = project_id
        WORKSPACE_DATA["data"]["relationships"] = WORKSPACE_PROJECT_REL

    js_data = json.dumps(WORKSPACE_DATA)

    headers = set_token(token)

    url = f"https://app.terraform.io/api/v2/organizations/{org}/workspaces"

    response = requests.post(url=url, data=js_data, headers=headers)
    check_response(response=response, resource="Workspace")
    click.echo(f"Workspace {name} successfully created")


def create_project(org: str, project_name: str, token: str, description: str = ""):
    
    click.echo(f"Attempting to create project {project_name}...\n")

    url = f"https://app.terraform.io/api/v2/organizations/{org}/projects"
    
    PROJ_DATA["data"]["attributes"]["name"] = project_name
    PROJ_DATA["data"]["attributes"]["description"] = description
    
    headers = set_token(token)

    js_data = json.dumps(PROJ_DATA)
    response =  requests.post(url=url, data=js_data, headers=headers)
    
    check_response(response=response, resource="Project")
    
    click.echo(f"Project {project_name} successfully created in {org} organization")


def create_agent(org: str, token:str, name: str):
    AGENT_POOL_DATA["data"]["attributes"]["name"] = name
    url = f"https://app.terraform.io/api/v2/organizations/{org}/agent-pools"
    headers = set_token(token)
    data = json.dumps(AGENT_POOL_DATA)

    response = requests.post(url=url, data=data, headers=headers)
    return response

def create_token(agent_id, token:str, description: str):
    url = f"https://app.terraform.io/api/v2/agent-pools/{agent_id}/authentication-tokens"
    headers = set_token(token)
    
    AGENT_TOKEN_DATA["data"]["attributes"]["description"] = description
    data = json.dumps(AGENT_TOKEN_DATA)
    response = requests.post(url=url, data=data, headers=headers)
    return response

def create_agent_token(agent_id: str, token:str, description: str):
    click.echo(f"Attempting to create agent token...\n")
    token_create_response = create_token(agent_id=agent_id, token=token, description=description)
    check_response(response=token_create_response, resource="Agent token")
    tok_res_js = token_create_response.json()
    token_val = tok_res_js["data"]["attributes"]["token"]
    click.echo(f"Agent token created, please copy its value, it will not be displayed again!!!\nTOKEN: {token_val}")

def create_agent_and_token(name: str, org:str, token:str, description: str, t):
    click.echo(f"Attempting to create agent {name}...\n")
    agent_create_response = create_agent(name=name, org=org, token=token)

    check_response(response=agent_create_response, resource="Agent pool")
    click.echo(f"Agent pool {name} successfully created in {org} organization")
    if t:
       #if create_token flag is set create token for associated agent and output value
       ag_res_js = agent_create_response.json()
       agent_id = ag_res_js["data"]["id"]
       create_agent_token(agent_id=agent_id, token=token, description=description)
