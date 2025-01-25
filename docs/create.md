# terrk create

**Create resources using command line args**


[terrk create agent](#terrk-create-agent)          
[terrk create agenttoken](#terrk-create-agenttoken)   
[terrk create project](#terrk-create-project)       
[terrk create team](#terrk-create-team)              
[terrk create teamtoken](#terrk-create-teamtoken)   
[terrk create workspace](#terrk-create-workspace)    


## terrk create agent

**Create Terraform agent, agent-token and output token**  

```
terrk create agent NAME [OPTIONS]
                        --description
                        --gen-token

```
### Required Arguments

```NAME```    
   The name to assign to the agentpool

### Optional Parameters
```-t, --gen-token```      
    if set will create and output agent token

```-d, --description```  
    Agent token description, must be set if -t flag is set  


## terrk create agenttoken

**Create Terraform agent-token and output token**

```
terrk create agenttoken --agent-id
                        --description
```

### Required Parameters

```-a, --agent-id```  
   The ID of the agentpool.  

```-d, --description```  
   Agent token description. This must be set.

## terrk create project

**Create Terraform cloud project**

```
terrk create project NAME --description
```
### Required Arguments

```NAME```  
   The name of the project.

### Optional Parameters

```-d, --description```  
   Project description.

## terrk create team

**Create Terraform cloud team [beta(untested)]**

```
terrk create team NAME --team-token
```

### Required Arguments

```NAME```  
   The name of the team.

### Optional Parameters

```-t, --team-token```  
   If set, will create and output a team token.

## terrk create teamtoken

**Create Terraform cloud team token [beta(untested)]**

```
terrk create teamtoken --team-id 
                       --days
```

### Required Parameters

```-t, --team-id```  
   The ID of the team.

### Optional Parameters

```-d, --days```  
   Number of days the token will be valid for. Defaults to 7.

## terrk create workspace

**Create Terraform cloud workspace**

```
terrk create workspace NAME --project-id 
                            --terraform-version 
                            --description 
                            --exec-mode 
                            --agent-id
```

### Required Arguments

```NAME```  
   The name of the workspace.

### Optional Parameters

```-p, --project-id```  
   ID of the project to deploy the workspace in. Defaults to "default project."

```--terraform-version```  
   The version of Terraform to use for this workspace. Defaults to "latest."

```-d, --description```  
   The workspace description.

```-e, --exec-mode```  
   Supported options: local, remote, agent. Defaults to "local."

```-a, --agent-id```  
   The ID of the agent pool to use if the execution mode is set to "agent."