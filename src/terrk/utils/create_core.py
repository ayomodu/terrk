import requests
import click
import json
from copy import deepcopy
from typing import Literal, Optional

from .constants import (PROJ_DATA, WORKSPACE_DATA,
                        WORKSPACE_PROJECT_REL,
                        HTTP_SUCCESS_CODES, AGENT_POOL_DATA,
                        AGENT_TOKEN_DATA, TEAM_DATA,
                        TEAM_TOKEN_DATA)

from .utility import set_token, check_response, set_token_expiry


def create_workspace(project_id: str,
                     name: str, 
                     agent_id: Optional[str], 
                     token: str, 
                     description: Optional[str],
                     org: str,
                     exec_mode: Literal["local", "remote", "agent" ],
                     terraform_version = Optional[str]
                    ):
    workspace_data = deepcopy(WORKSPACE_DATA)
    workspace_project_rel = deepcopy(WORKSPACE_PROJECT_REL)

    workspace_data["data"]["attributes"]["description"] = description
    workspace_data["data"]["attributes"]["execution-mode"] = exec_mode
    workspace_data["data"]["attributes"]["name"] = name

    if exec_mode == "agent":
        workspace_data["data"]["attributes"]["agent-pool-id"] = agent_id

    if terraform_version:
        workspace_data["data"]["attributes"]["terraform-version"] = terraform_version

    if project_id:
        workspace_project_rel["project"]["data"]["id"] = project_id
        workspace_data["data"]["relationships"] = workspace_project_rel

    js_data = json.dumps(workspace_data)

    headers = set_token(token)

    url = f"https://app.terraform.io/api/v2/organizations/{org}/workspaces"
    
    response = requests.post(url=url, data=js_data, headers=headers)
    check_response(response=response, resource="Workspace")
    click.echo(f"Workspace {name} successfully created")


def create_project(org: str, project_name: str, token: str, description: str = ""):

    url = f"https://app.terraform.io/api/v2/organizations/{org}/projects"
    
    proj_data = deepcopy(PROJ_DATA)

    proj_data["data"]["attributes"]["name"] = project_name
    proj_data["data"]["attributes"]["description"] = description
    
    headers = set_token(token)

    js_data = json.dumps(proj_data)
    response =  requests.post(url=url, data=js_data, headers=headers)
    
    check_response(response=response, resource="Project")
    
    click.echo(f"Project {project_name} successfully created in {org} organization")


def create_agent(org: str, token:str, name: str):
    agent_pool_data = deepcopy(AGENT_POOL_DATA)

    agent_pool_data["data"]["attributes"]["name"] = name
    url = f"https://app.terraform.io/api/v2/organizations/{org}/agent-pools"
    headers = set_token(token)
    
    data = json.dumps(agent_pool_data)

    response = requests.post(url=url, data=data, headers=headers)
    return response

def create_token(agent_id, token:str, description: str):
    url = f"https://app.terraform.io/api/v2/agent-pools/{agent_id}/authentication-tokens"
    headers = set_token(token)
    
    agent_token_data = deepcopy(AGENT_TOKEN_DATA)

    agent_token_data["data"]["attributes"]["description"] = description
    data = json.dumps(agent_token_data)
    response = requests.post(url=url, data=data, headers=headers)
    return response

def create_agent_token(agent_id: str, token:str, description: str):
    token_create_response = create_token(agent_id=agent_id, token=token, description=description)
    check_response(response=token_create_response, resource="Agent")
    tok_res_js = token_create_response.json()
    token_val = tok_res_js["data"]["attributes"]["token"]
    click.echo(f"Agent token created, please copy its value, it will not be displayed again!!!\nTOKEN: {token_val}")

def create_agent_and_token(name: str, org:str, token:str, description: str, t):
    agent_create_response = create_agent(name=name, org=org, token=token)

    check_response(response=agent_create_response, resource="Agent pool")
    click.echo(f"Agent pool {name} successfully created in {org} organization")
    if t:
       #if create_token flag is set create token for associated agent and output value
       ag_res_js = agent_create_response.json()
       agent_id = ag_res_js["data"]["id"]
       create_agent_token(agent_id=agent_id, token=token, description=description)

def create_team(org: str,token: str, name: str):
    team_data = deepcopy(TEAM_DATA)
    team_data["data"]["attributes"]["name"] = name
    url = f"https://app.terraform.io/api/v2/organizations/{org}/teams"
    headers = set_token(token)
    data = json.dumps(team_data)
    response = requests.post(url=url, data=data, headers=headers)
    return response

def create_team_token(team_id: str, token: str, days: int):
    expiry_time = set_token_expiry(days=days)
    team_token_data = deepcopy(TEAM_TOKEN_DATA)
    team_token_data["data"]["attributes"]["expired-at"] = expiry_time
    url = f"https://app.terraform.io/api/v2/teams/{team_id}/authentication-token"
    headers = set_token(token)
    data = json.dumps(team_token_data)
    response = requests.post(url=url, data=data, headers=headers)
    check_response(response=response, resource="Team TOKEN")
    tok_res_js = response.json()
    token_val = tok_res_js["data"]["attributes"]["token"]
    click.echo(f"Team token created, please copy its value, it will not be displayed again!!!\nTOKEN: {token_val}")

def create_team_and_token(name: str, org:str, token:str, t):
    team_resp = create_team(name=name, org=org, token=token)
    check_response(response=team_resp, resource="Team")
    click.echo(f"Team {name} successfully created")
    if t:
    #if create_token flag is set create token for associated team and output value
        days = click.prompt("Enter the number of days the token will be valid for", type=int)    
        team_res_js = team_resp.json()
        team_id = team_res_js["data"]["id"]
        create_team_token(team_id=team_id, token=token, days=days)


