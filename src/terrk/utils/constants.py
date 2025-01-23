from typing import Optional
from pydantic import BaseModel

class WorkspaceObj(BaseModel):
    WorkspaceName: str
    ExecutionMode: str
    projectid: Optional[str] = None
    AgentID: Optional[str] = None
    Description: Optional[str] = None

class ExcelWorkspaceObj(WorkspaceObj):
    No: int


PROJ_DATA = {
                    "data": {
                    "type": "projects",
                    "attributes": {
                        "name": "",
                        "description": ""
                        }
                    }
            }

WORKSPACE_DATA = {
                    "data": {
                        "type": "workspaces",
                        "attributes": {
                            "name": "",
                            "execution-mode": "",
                            "description": "",
                            "working-directory": "",
                            "source-name" : "terrk"
                        }

                    }
                }

HEADERS = {
            "Authorization": "",
            "Content-Type": "application/vnd.api+json"
          }

VCS_CONFIG = {
    "tags-regex": "",
    "oauth-token-id": "",
    "ingress-submodules": "",
    "identifier": "",
    "branch": ""
}

AGENT_POOL_DATA = {
                "data": {
                    "type": "agent-pools",
                    "attributes": {
                        "name": "",
                        "organization-scoped": True,
                    }
                }
            }

AGENT_TOKEN_DATA = {
                    "data": {
                        "type": "authentication-tokens",
                        "attributes": {
                        "description":""
                        }
                    }
                    }

WORKSPACE_PROJECT_REL =  {
                        "project": {
                            "data": {
                                "type": "projects",
                                "id": ""
                            }
                        }
                }

TEAM_DATA = {
            "data": {
                "type": "teams",
                "attributes": {
                "name": ""
                    }
                }
            }

TEAM_TOKEN_DATA =   {
                    "data": {
                        "type": "authentication-token",
                        "attributes": {
                            "expired-at": ""
                            }
                        }
                    }

HTTP_SUCCESS_CODES = {200,201,202,203,204}

SUPPORTED_FILE_TYPE = {".xlsx", ".yaml", ".yml"}

WORKSPACE_DEPLOYMENT_SCHEMA_EXCEL = {
                "type": "object",
                "required": ['No', 'WorkspaceName', 'ExecutionMode'],
                "additionalProperties": False,
                "properties": {
                    "No" : {"type": "number"},
                    "WorkspaceName": {"type": "string"},
                    "ExecutionMode": {"type": "string", "enum": ["local", "remote", "agent"]},
                    "ProjectID": {"type": "string"},
                    "AgentID" : {"type": "string"},
                    "Description" : {"type": "string"},
                    "Version": {"type": "string"}
                    }

}

WORKSPACE_DELETE_SCHEMA_EXCEL = {
                "type": "object",
                "required": ['No', 'WorkspaceName'],
                "additionalProperties": False,
                "properties": {
                    "No" : {"type": "number"},
                    "WorkspaceName": {"type": "string"}
                    }

}

WORKSPACE_DEPLOYMENT_SCHEMA_YAML = {
                "type": "object",
                "required": ['kind', 'resource'],
                "additionalProperties": False,
                "properties": {
                    "kind" : {"type": "string", "enum": ["workspace"]},
                    "resource" : {
                        "type": "object",
                        "required": ["name", "execMode", "projectid", "agentid", "description", "version"],
                        "additionalProperties": False,
                        "properties": {
                            "name": {"type": "string"},
                            "execMode": {"type": "string", "enum": ["local", "remote", "agent"]},
                            "projectid": {"type": "string"},
                            "agentid" : {"type": "string"},
                            "description" : {"type": "string"},
                            "version" : {"type": "string"}

                        }
                    }
                    
                    }

}

WORKSPACE_DELETE_SCHEMA_YAML = {
                "type": "object",
                "required": ['kind', 'resource'],
                "additionalProperties": False,
                "properties": {
                    "kind" : {"type": "string", "enum": ["workspace"]},
                    "resource" : {
                        "type": "object",
                        "required": ["name"],
                        "additionalProperties": False,
                        "properties": {
                            "name": {"type": "string"}

                        }
                    }
                    
                    }

}