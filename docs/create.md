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

## terrk create team

## terrk create teamtoken

## terrk create workspace