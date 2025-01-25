# Terrk Context Management Commands 

## terrk init

**Initialize the configuration needed to work with TFC, takes the name of your TFC ORG as an argument.**  

```
terrk init ORG --token
```

### Required Arguments

```ORG```  
   Your Terraform Cloud organization name.

### Optional Parameters

```-t, --token```  
   Authentication token for Terraform Cloud.

## terrk which

**Show the current context**  

```
terrk which
```

# terrk config

**Manage terrk context configuration**  

**NB: Contexts here refer to TFC organization configurations the required details to access the Org (Org_name and API token)**  

## terrk config clean  

**Remove all contexts - deletes the config file**  

```
terrk config clean
```

## terrk config lscontext 

**List all available contexts in the config file**  

```
 terrk config lscontext
```
## terrk config rmcontext 

**Remove a context from config file**  

```
 terrk config rmcontext NAME
```
### Required Arguments

```NAME```    
   The name of the TFC organization/context to remove from config file

## terrk config switch 

**Switch to alternate context**  

```
 terrk config switch NAME
```
### Required Arguments

```NAME```    
   The name of the TFC organization/context to switch to