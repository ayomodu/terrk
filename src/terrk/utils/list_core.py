from .utility import set_token, check_response
import requests
from prettytable import PrettyTable
import click

def list_projects(number, org, token):
    headers = set_token(token)
    url = f"https://app.terraform.io/api/v2/organizations/{org}/projects"
    query_params = {"page[size]" : number}
    response = requests.get(url=url, params=query_params, headers=headers)
    check_response(response=response, resource='Project')
    response_js = response.json()
    table_headers = ["No", "Projects", "Project_id"]
    
    table = PrettyTable(table_headers)

    for no, data in enumerate(response_js["data"]):
        table.add_row([no+1, data["attributes"]["name"], data["id"]])

    click.echo(table)

def list_workspaces(project_id, number, org, token):
    headers = set_token(token)
    url = f"https://app.terraform.io/api/v2/organizations/{org}/workspaces"
    query_params = {"page[size]" : number,
                    "filter[project][id]": project_id
                    }
    response = requests.get(url=url, params=query_params, headers=headers)
    check_response(response=response, resource='Workspaces')
    response_js = response.json()
    table_headers = ["No", "Workspaces", "Id", "ExecMode"]
    
    table = PrettyTable(table_headers)

    for no, data in enumerate(response_js["data"]):
        table.add_row([no+1, data["attributes"]["name"], data["id"], data["attributes"]["execution-mode"] ])

    click.echo(table)

def list_agents(number, org, token):
    headers = set_token(token)
    url = f"https://app.terraform.io/api/v2/organizations/{org}/agent-pools"
    query_params = {"page[size]" : number
                    }
    response = requests.get(url=url, params=query_params, headers=headers)
    check_response(response=response, resource='Workspaces')
    response_js = response.json()
    table_headers = ["No", "Agent Pools", "Id"]
    
    table = PrettyTable(table_headers)

    for no, data in enumerate(response_js["data"]):
        table.add_row([no+1, data["attributes"]["name"], data["id"]])

    click.echo(table)

def list_teams(number, org, token):
    headers = set_token(token)
    url = f"https://app.terraform.io/api/v2/organizations/{org}/teams"
    query_params = {"page[size]" : number
                    }
    response = requests.get(url=url, params=query_params, headers=headers)
    check_response(response=response, resource='Workspaces')
    response_js = response.json()
    table_headers = ["No", "Teams", "Id"]
    
    table = PrettyTable(table_headers)

    for no, data in enumerate(response_js["data"]):
        table.add_row([no+1, data["attributes"]["name"], data["id"]])

    click.echo(table)