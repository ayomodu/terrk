# terrk delete

**Delete TFC resources**  

[terrk delete agent](#terrk-delete-agent)    
[terrk delete project](#terrk-delete-project)   
[terrk delete team](#terrk-delete-team)       
[terrk delete workspace](#terrk-delete-workspace)  


## terrk delete agent

**Delete Terraform cloud agent pool**  

```
terrk delete agent AGENT_POOL_ID
```
### Required Arguments

```AGENT_POOL_ID```  
   The ID of the agent pool to delete


## terrk delete project    

**Delete Terraform cloud project**  

```
terrk delete project PROJECT_ID
```
### Required Arguments

```PROJECT_ID```  
   The ID of the project to delete

## terrk delete team

**Delete Terraform cloud team [beta(untested)]**  

```
terrk delete team TEAM_ID
```
### Required Arguments

```TEAM_ID```  
   The ID of the team to delete

## terrk delete workspace

**Delete Terraform cloud workspace/workspaces**  

```
terrk delete workspace --file 
                       --name
```

**NB you have to provide either one of --name or --file for each execution of this command. Providing both options or none of the options will fail with the appropriate error message**  

### Optional Parameters

```-f, --file```  
   Config file with a list of workspaces to delete.

```-n, --name```  
   Name of the workspace to delete.

**To review the accepted file types and config formats review the [documentation here](config_file_formats.md)**