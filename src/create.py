import requests
import click
import json
import sys

from typing import Literal, Optional

from .constants import PROJ_DATA, WORKSPACE_DATA ,HEADERS, WORKSPACE_PROJECT_REL, HTTP_SUCCESS_CODES


def set_token(token):
    context_token = "Bearer " + str(token)
    HEADERS["Authorization"] = context_token

    return HEADERS


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

    if response.status_code not in HTTP_SUCCESS_CODES:
        reason = (response.json()['errors'][0]['detail']).lower()
        sys.stderr.write(f"Error!!! Status code: {response.status_code}, Workspace {reason}\n")
        exit(1)
        return
    click.echo(f"Workspace {name} successfully created")


def create_project(org: str, project_name: str, token: str, description: str = ""):
    
    click.echo(f"Attempting to create project {project_name}...\n")

    url = f"https://app.terraform.io/api/v2/organizations/{org}/projects"
    
    PROJ_DATA["data"]["attributes"]["name"] = project_name
    PROJ_DATA["data"]["attributes"]["description"] = description
    
    headers = set_token(token)

    js_data = json.dumps(PROJ_DATA)
    response =  requests.post(url=url, data=js_data, headers=headers)
    if response.status_code not in HTTP_SUCCESS_CODES:
        reason = (response.json()['errors'][0]['detail']).lower()
        sys.stderr.write(f"Error!!! Status code: {response.status_code}, Project {reason}\n")
        exit(1)
        return
    click.echo(f"Project {project_name} successfully created in {org} organization")

    
    
    