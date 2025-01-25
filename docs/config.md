# terrk config

**Manage terrk context configuration**  

**NB: Contexts here refer to TFC organization configurations the required details to access the Org (Org_name and API token)**  

## terrk config clean  

**Remove all contexts - deletes the config file**  

```
terrk config clean
```

## terrk config lscontext 

**List all available contexts in config file**  

```
 terrk config lscontext
```
## terrk config rmcontext 

**Remove a context[TFC Organization] from config file**  

```
 terrk config rmcontext NAME
```
### Required Argument

```NAME```    
   The name of the TFC organization context to remove from config file

## terrk config switch 

**Switch to alternate context**  

```
 terrk config switch NAME
```
### Required Argument

```NAME```    
   The name of the TFC organization context to switch to