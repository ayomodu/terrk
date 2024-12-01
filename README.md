`A simple and intuitive cli application to enable the deployment of resources to Terraform cloud.`

`'''
~Supported operations

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
create a worksocae in current context
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

DELETE
```~