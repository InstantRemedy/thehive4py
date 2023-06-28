from ..exceptions.HiveException import *
from ..responces.CaseTemplateResponce import *
from ..requests.AbstractRequest import *
from ..models.CaseTemplate import *

import requests as _requests

class CaseTemplateRequest(AbstractRequest):
    def __init__(self, session: _requests.Session, url: str):
        super().__init__(session, url)
        
    def get_all(self, name_organisation: str) -> tuple[list[CaseTemplate], CaseTemplateResponce]: 
        json = {
            "query": [
                {
                    "_name": "getOrganisation",
                    "idOrName": f"{name_organisation}"
                },
                {
                    "_name": "caseTemplates"
                },
                {
                    "_name": "sort",
                    "_fields": [
                        {
                            "displayName": "asc"
                        }
                    ]
                },
                {
                    "_name": "page",
                    "from": 0,
                    "to": 999
                }
            ]
        }
        
        responce = self._post("api/v1/query", json, CaseTemplateResponce)
        
        cases = []
        for caseResponce in responce.content:
            cases.append(CaseTemplate(caseResponce))
        
        return cases, responce
    
    def create(self,
               name: str,
               description: str,
               title_prefix: str = "",
               severity: int = 0,
               tlp: int = 0,
               pap: int = 0,
               tags: list[str] = [],
               tasks: list[dict] = [],
               custom_fields: dict = {},
               display_name: str = ""
               ) -> CaseTemplateResponce:
        
        json = {
            "name": name,
            "description": description,
            "titlePrefix": title_prefix,
            "severity": severity,
            "tlp": tlp,
            "pap": pap,
            "tags": tags,
            "task": tasks,
            "customFields": custom_fields,
            "description": description,
            "displayName": display_name
        }
        
        return self._post("api/case/template", json, CaseTemplateResponce)
    
    def update(self, 
                id_name: str,
                display_name: str,
                tlp: int = 0,
                tasks: list[dict] = []) -> CaseTemplateResponce:
        json = {
            "displayName": display_name,
            "tlp": tlp,
            "tasks": tasks
        }
        
        return self._patch(f"api/case/template/{id_name}", json, CaseTemplateResponce)
    
    def delete(self, id_name: str) -> CaseTemplateResponce:
        return self._delete(f"api/case/template/{id_name}", CaseTemplateResponce)