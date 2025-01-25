# terrk list

**List Terraform cloud resources**  

[terrk list agents](#terrk-list-agents)    
[terrk list projects](#terrk-list-projects)   
[terrk list teams](#terrk-list-teams)       
[terrk list workspaces](#terrk-list-workspaces)


## terrk list agents 

**List agent pools in Terraform cloud organization**

```
terrk list agents --number
```


### Optional Parameters

```-n, --number```  
   Number of results to display. Defaults to 10.

## terrk list projects 

**List projects in Terraform cloud organization**

```
terrk list projects --number
```


### Optional Parameters

```-n, --number```  
   Number of results to display. Defaults to 20.


## terrk list teams  

**List teams in Terraform cloud organization [beta(untested)]**

```
terrk list teams --number
```


### Optional Parameters

```-n, --number```  
   Number of results to display. Defaults to 10.


## terrk list workspaces

**List workspaces in Terraform cloud organization**

```
terrk list workspaces --project-id 
                      --number
```

### Required Parameters
```-p, --project-id```
    Project ID to filter results by 

### Optional Parameters

```-n, --number```  
   Number of results to display. Defaults to 20.
