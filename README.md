
# Terrk: A simple and intuitive command-line interface (CLI) application for managing resources in Terraform cloud.

Description

## Features

- **Create Resources (Workspaces, Projects, Agent Pools, Agent tokens, Teams(beta), Team tokens(beta))**: Easily create new namespaces in your Kubernetes cluster.
- **List Namespaces**: Display a list of all existing namespaces.
- **Delete Namespaces**: Remove namespaces that are no longer needed.

## Prerequisites

Before using AYONS, ensure that you have the following installed:

- **Kubernetes Cluster**: A running Kubernetes cluster.
- **kubectl**: Command-line tool for interacting with the Kubernetes API server.
- **Bash**: AYONS is implemented as a Bash script; ensure that Bash is available on your system.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ayomodu/ayons.git

```
Supported operations

INIT
inititialize/save context and create config file
    terrk init ORG_NAME
    options:
        token: -t, --token api_key needed to access TFC 

SWITCH
switch to alternate context
    terrk switch CONTEXT(NAME OF ORG)

WHICH
show the current context
terrk which

CREATE
create a workspace in current context
terrk create workspace WORKSPACE
    arg: WORKSPACE NAME
    options:
      description: --description, -d
      project: --project, -p (default=default project)

terrk create project PROJECT
    arg: PROJECT NAME
    options:
      description: --description, -d

terrk create team TEAM
    arg: TEAM NAME

terrk apply 
    arg: FILE NAME
    options:
      --type, -t
      --file, -f

DELETE```

apply highlevel steps
check file is valid(in supported file types)
depending on file type run:
    parser function for respective file type
    validate resource type to deploy:
        validate fields in file
            deploy resource


pip install -r requirements.txt
pip install .

pyinstaller --name terrk --onefile --console src/terrk/__main__.py
