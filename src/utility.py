import sys  
from typing import Optional
import click
import json
import os
from pathlib import Path
import datetime 

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
    if not check_config():
        sys.stderr.write("No contexts saved, run 'terrk init' to add contexts\n")
        exit(1)
        return
    config = read_config()
    if name not in config["contexts"]:
        sys.stderr.write(f"Context not found, run 'terrk init {name}' to add context\n")
        exit(1)
        return
    update_context(name)
    click.echo(f"Context switched to {name}")
    return


