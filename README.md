
# Terrk: A simple and intuitive command-line interface (CLI) application for managing resources in Terraform cloud (TFC).

## Description
Terrk provides a simple and familair way of managing resources in TFC.  
It is a cli application that acts as a client of the Terraform cloud API to bulk create, delete and list terraform cloud infrastructure resources offering an alternative method of managing these resources outside of the UI and via HCL terraform code.  
We also have context management built-in to enable you manage infra resources across multiple Terraform organizations by simply switching between contexts (Organizations).  
## Features

- **Create TFC Resources (Workspaces, Projects, Agent Pools, Agent tokens, Teams(beta), Team tokens(beta))** : Create resources using cli arguments and yaml/excel configuration files
- **List Resources**: Display a list of existing resources.
- **Delete Resources**: Remove namespaces that are no longer needed.
- **Add TFC organizations**

## Prerequisites

Before using terrk, ensure that you have a:

- **Terraform Cloud Org**: A Terraform cloud Organization

## Installation
**NB: Terrk has been tested and is only supported on x64 (Windows) and x86_64(Linux) bit systems** 
1. **Download the Binary File:**:

   Download the binary for you OS type here

### Windows Install
   Adding the program's directory to the system PATH allows you to run the executable from any command prompt without specifying its full path.
#### **Steps:**
  -  1. **Press Win + X and select System.**
  -  2. **Click on Advanced system settings.**
  -  3. **In the System Properties window, go to the Advanced tab and click on Environment Variables.**
  -  4. **In the Environment Variables window, find the Path variable under System variables, select it, and click Edit.**
  -  5. **Click New and add the path to the directory you have the terrk executable in, e.g., C:\Program Files\Desktop\terrk.**
  -  6. **Click OK to close all windows.**
  -  7. **Open a new CMD prompt window and run ```terrk --verison``` , you should see output similar to;** 
    ```terrk, version 0.1.0```

### Linux Install
####   **Steps:**
   - **1. Ensure bin file is executable using command:** 
        ```chmod +x terrk```
   - **2. Move terrk executable to /usr/local/bin/:**
        ```mv terrk /usr/local/bin/```
   - **3. run ```terrk --verison``` , you should see output similar to;** 
    ```terrk, version 0.1.0```

## Getting Started

### Initialize Context
To begin using terrk you have to first generate a User api token in your TFC organization.  
To understand how TFC user tokens work and how to generate them review the terraform documentation [here](https://developer.hashicorp.com/terraform/cloud-docs/users-teams-organizations/users#tokens)    

Next run  
```
terrk init ORG_NAME
```
This creates a context for your organization and will prompt you to provide the API token generated above.  

**NB: The token is treated as a secret and will not be visible in the terminal when you paste it following the prompt.**     

This command also allows you specify the ```-t``` option to provide the token. We advise against doing this as it makes the API token visible in command history.  


### Create Resources

To begin creating TFC resources you can use the top level ```terrk create``` command with the correponding sub-command.  

```
terrk create project myproject
```

Creates a new TFC project named "myproject" in your Terraform cloud organization.  

```
terrk create workspace myworkspace -p PROJECT_ID
```
Creates a workspace named "myworkspace" in the project with PROJECT_ID specified in the command.  

**NB: The -p flag here is optional. If you do not specify a PROJECT_ID, the workspace is automatically created in the default project of your TFC organization.**  

### List Resources

terrk supports obtaining a list of a specific type of resource.  

E.g.    

**List projects in TFC organization**   

The command  
```
terrk list projects
```
Produces the output below  

| No   |     Projects    |      Project_id      |
| ---  | --------------- | -------------------- |
|  1   | Default Project | prj-kod1j4fmT5p4bsoJ |
|  2   |    myproject    | prj-9U1TyEnsQXLEKrrk |


**List workspaces in a project**    

The command
```
terrk list workspaces -p PROJECT_ID
```
Produces the output below  

| No  |        Workspaces       |          Id         | ExecMode |
| --- | ----------------------- | ------------------- | -------- |
| 1   |         newlinux        | ws-PCv9RdRm8ekwMLMc |  local   |
| 2   |           init          | ws-uBbwUzJpvdjcgkRm |  local   |




terrk also supports bulk creating and deleting specific resources (workspaces).  
To see the full list of supported operations review the [documentation here]()

### Delete Resources

terrk enables you delete resources.  

**Delete Project**  

The command below deletes the project with projectid PROJECT_ID

```
terrk delete project PROJECT_ID
```

**Delete Workspace**  

The command below deletes the workspace with name WORKSPACENAME  

```
terrk delete workspace WORKSPACENAME
```
 

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
