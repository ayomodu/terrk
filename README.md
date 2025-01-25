
# Terrk: A simple and intuitive command-line interface (CLI) application for managing resources in Terraform cloud (TFC).

## Description
Terrk provides a simple and familiar way of managing resources in TFC.  
It is a cli application that acts as a client of the Terraform cloud API to bulk create, delete and list Terraform cloud resources offering an alternative method of managing these resources outside of the UI or via HCL terraform code.  
terrk is context aware and enables you manage TFC resources across multiple Terraform cloud organizations by simply switching between contexts (Organizations).  
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

The command above also allows you specify the ```-t``` option to provide the token. We advise against doing this as it makes the API token visible in command history.  


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
| 3   |           test          | ws-vPbwGzJherjklsFx |  agent   |


### Delete Resources

terrk enables you delete resources.  

**Delete Project**  

The command below deletes the project with projectid PROJECT_ID

```
terrk delete project PROJECT_ID
```

**Delete Workspace**  

The command below deletes the workspace with name WORKSPACE_NAME  

```
terrk delete workspace WORKSPACE_NAME
```
 
**NB: terrk also supports bulk creating and deleting specific resources (workspaces) using excel and yaml configuration files.**      


**To see the list of supported operations run ```terrk``` then you can drill down to the commands, subcommands and their associated options using the ```--help``` option.**      

```
C:\Users\ayomodu>terrk

Usage: terrk [OPTIONS] COMMAND [ARGS]...

  A tool to manage TFC resources

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  apply   Create resource using a yaml or xlsx file
  config  Manage context configuration
  create  Create resources using command line args
  delete  Delete TFC resources
  init    Initialize the configuration needed to work with TFC
  list    List Terraform cloud resources
  which   Show the current context
```

## Further reading

To see the full list of commands, sub-commands and configuration options review the [documentation here](docs/root.md)

