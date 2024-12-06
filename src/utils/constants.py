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
                        "organization-scoped": False,
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

SUPPORTED_FILE_TYPE = [".xslx", ".yaml", ".yml"]