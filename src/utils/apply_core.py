from pathlib import Path
import sys
import click
from .utility import validate_config, get_workspace_config
from .constants import WORKSPACE_DEPLOYMENT_SCHEMA_EXCEL, WORKSPACE_DEPLOYMENT_SCHEMA_YAML
from .create_core import create_workspace
import pandas as pd
from typing import Optional


def validate_and_deploy_excel(workspace_config, org, token):
    for config in workspace_config:
        validate_config(schema=WORKSPACE_DEPLOYMENT_SCHEMA_EXCEL, config=config)
        create_workspace(project_id = config["ProjectID"],
                     name=config['WorkspaceName'], 
                     agent_id=config["AgentID"], 
                     token=token, 
                     description=config["Description"],
                     org=org,
                     exec_mode=config["ExecutionMode"],
                     terraform_version = config["Version"])

def validate_and_deploy_yaml(workspace_config, org, token):
    for config in workspace_config:
        validate_config(schema=WORKSPACE_DEPLOYMENT_SCHEMA_YAML, config=config)
        create_workspace(project_id = config["resource"]["projectid"],
                     name=config["resource"]["name"], 
                     agent_id=config["resource"]["agentid"], 
                     token=token, 
                     description=config["resource"]["description"],
                     org=org,
                     exec_mode=config["resource"]["execMode"],
                     terraform_version = config["resource"]["version"])

def validate_and_deploy_workspace(file, org, token):
    workspace_config, file_ext = get_workspace_config(file=file)
    if file_ext == ".xlsx":
        validate_and_deploy_excel(workspace_config, org=org, token=token)
        return
    if file_ext == ".yaml" or ".yml":
        validate_and_deploy_yaml(workspace_config, org, token)
        return
    

    
