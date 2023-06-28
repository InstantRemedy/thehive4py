from ..exceptions.HiveException import *
from ..responces.CustomFieldResponce import *
from ..requests.AbstractRequest import *
from ..models.CustomField import *

import requests as _requests

class CustomFieldRequest(AbstractRequest):
    def __init__(self, session: _requests.Session, url: str):
        super().__init__(session, url)
    
    #id != name
    def get(self, id: str) -> tuple[CustomField, CustomFieldResponce]:         
        
        responce = self._get(f"api/customField/{id}", CustomFieldResponce)
        
        return CustomField(responce.content), responce
        
    def get_all(self) -> tuple[list[CustomField], CustomFieldResponce]:
        responce = self._get("api/customField", CustomFieldResponce)
        
        customFields = []
        
        for customFieldResponce in responce.content:
            customFields.append(CustomField(customFieldResponce))
        
        return customFields, responce
    
    def create(self,
               name: str,
               reference: str,
               description: str,
               type: str,
               mandatory: bool,
               options: list[str]) -> CustomFieldResponce:
        json = {
            "name": name,
            "reference": reference,
            "description": description,
            "type": type,
            "mandatory": mandatory,
            "options": options
        }
        
        return self._post("api/customField", json, CustomFieldResponce)
    
    def update(self, 
                id: str,
                new_name: str,
                new_reference: str,
                new_description: str,
                new_type: str,
                new_mandatory: bool,
                new_options: list[str]
               ) -> CustomFieldResponce:
        
        json = {
            "name": new_name,
            "reference": new_reference,
            "description": new_description,
            "type": new_type,
            "mandatory": new_mandatory,
            "options": new_options
        }

        return self._patch(f"api/customField/{id}", json, CustomFieldResponce)
    
    #id != name
    def delete(self, id: str) -> CustomFieldResponce:
        return self._delete(f"api/customField/{id}")
    
    #id != name
    def use_count(self, id: str) -> tuple[dict, CustomFieldResponce]:
        responce = self._get(f"api/customField/{id}/use", CustomFieldResponce)
        
        return responce.content, responce