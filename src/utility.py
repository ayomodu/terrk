import sys  
from typing import Optional
import click
import json
import os
from pathlib import Path
import datetime 
from .constants import HEADERS, HTTP_SUCCESS_CODES

CONFIG_DIR = Path().home() / ".terrk"
CONFIG_FILE_PATH = CONFIG_DIR / ".terrk.conf"

def check_config(filename: str = CONFIG_FILE_PATH) -> bool:
    file_path = Path(filename)
    if file_path.exists():
        return True
    return False

def read_config(filename: str = CONFIG_FILE_PATH):
    with open(filename, 'r') as file:
        file_content = json.load(file)
        file.close
        return file_content


def check_context(context_obj):
    if not context_obj:
        click.echo("No context available. Please run 'terrk init' first")
        exit(1)
        return

def create_config(org: str, token: str, file_path: str = CONFIG_FILE_PATH):
    '''Create a config file and add the new context
                    Triggered on an init '''
    file_content = {}
    file_content.update({
        "created_at": str(datetime.datetime.now()),
        "contexts" : {
            org : {
                "api_token": token,
                "Last_updated": str(datetime.datetime.now())
                  }
                    }
            
            })
    with open(file_path, 'w') as file:
        json.dump(file_content, file, indent=4)



def update_config(org, token, file_path: str = CONFIG_FILE_PATH):
    '''Update the existing context in the config file with the new config details (api_token)'''
    file_content = read_config(file_path)

    if org in file_content["contexts"]:
        click.echo(f"Context {org} already exists updating config")
    file_content["contexts"].update(
        { org : {
                "api_token": token,
                "Last_updated": str(datetime.datetime.now())
                }
        }       
            )
    with open(file_path, 'w') as file:
        json.dump(file_content, file, indent=4)

def update_context(org):
    with open(CONFIG_FILE_PATH, "r") as file:
        file_content = json.load(file)
        file_content.update({
            "current" : org
        })
        file.close
    with open(CONFIG_FILE_PATH, "w") as file:
        json.dump(file_content, file, indent=4)

def clean_context(context_obj):
    if os.path.exists(CONFIG_FILE_PATH):
        os.remove(CONFIG_FILE_PATH)
        click.echo("terrk context cleaned!!!")
        if context_obj:
            context_obj.clear()
        return
    click.echo("no terrk context to clean up")
    return

def extract_context():
    config_file_path = Path(CONFIG_FILE_PATH)
    if config_file_path.exists():
        with open(config_file_path, 'r') as file:
            content = json.load(file)
            cur_ctx = content["current"]
            token = content['contexts'][cur_ctx]["api_token"]
            return cur_ctx, token
    return ""


def get_context_detail(context_obj):
    context = ''.join(context_obj.keys())
    token = context_obj[context]
    return context, token

def set_token(token):
    context_token = "Bearer " + str(token)
    HEADERS["Authorization"] = context_token

    return HEADERS

def check_response(response, resource: str):
    if response.status_code not in HTTP_SUCCESS_CODES:
        reason = (response.json()['errors'][0]['detail']).lower()
        sys.stderr.write(f"Error!!! Status code: {response.status_code}, {resource} {reason}\n")
        exit(1)
        return
