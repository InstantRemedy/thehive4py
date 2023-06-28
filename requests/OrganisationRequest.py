from ..exceptions.HiveException import *
from ..responces.OrganisationResponce import *
from ..requests.AbstractRequest import *
from ..models.Organisation import *

import requests as _requests

class OrganisationRequest(AbstractRequest):
    def __init__(self, session: _requests.Session, url: str):
        super().__init__(session, url)
    
    def create(self, name: str, description: str) -> tuple[Organisation, OrganisationResponce]:
        json = {
            "name": name,
            "description": description
        }
        
        responce = self._post("api/organisation", json, OrganisationResponce)
        organisation = Organisation(responce.content)

        return organisation, responce
        
    def update(self, id: str, name: str, description: str) -> OrganisationResponce:
        json = {
            "name": name,
            "description": description
        }
        
        responce = self._patch(f"api/organisation/{id}", json, OrganisationResponce)
        
        return responce     
    
    def get_all(self) -> tuple[list[Organisation], OrganisationResponce]:
        json = {
            "query" : [
                {
                    "_name" : "listOrganisation"
                },
                {
                    "_name" : "sort",
                    "_fields" : [
                            {
                                "_updatedAt" : "desc"
                            } 
                    ]
                },
                {
                    "_name" : "page",
                    "from" : 0, 
                    "to" : 9999
                }
            ]
        }
        
        responce = self._post("api/v1/query", json, OrganisationResponce)
        organisations = []
        
        for organisation_json in responce.content:
            organisations.append(Organisation(organisation_json))
        
        return organisations, responce
    
    def get(self, id : str) -> tuple[Organisation, OrganisationResponce]:
        responce = self._get(f"api/organisation/{id}", OrganisationResponce)
        organisation = Organisation(responce.content)
        
        return organisation, responce