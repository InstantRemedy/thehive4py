from ..exceptions.HiveException import *
from ..responces.UserResponce import *
from .AbstractRequest import *
from ..models.User import *

import requests as _requests

class UserRequest(AbstractRequest):
    def __init__(self, session: _requests.Session, url: str):
        super().__init__(session, url)
    
    def get(self, id: str) -> tuple[User, UserResponce]:
        responce = self._get(f"api/v1/user/{id}", UserResponce)
        user = User(responce.content)
        
        return user, responce
    
    def get_all(self, name_organisation: str) -> tuple[list[User], UserResponce]:
        
        json =  {
            "query": [
                {
                "_name": "getOrganisation",
                "idOrName": f"{name_organisation}"
                },
                {
                "_name": "users"
                },
                {
                "_name": "sort",
                "_fields": [
                    {
                    "login": "asc"
                    }
                ]
                },
                {
                "_name": "page",
                "from": 0,
                "to": 999,
                "organisation": "StrangeBee"
                }
            ]
        }
        responce = self._post(f"api/v1/query", json, UserResponce)

        users = []
        
        for user_json in responce.content:
            users.append(User(user_json))
        
        return users, responce
    
    def update(self, 
               id: str, 
               name: str, 
               profile: str, 
               organisation: str, 
               locked: bool
            ) -> UserResponce:   
        
        json = {
            "name": name,
            "profile": profile,
            "organisation": organisation,
            "locked": locked   
        }
        
        responce = self._patch(f"api/v1/user/{id}", json, UserResponce)
        
        return responce
    
    def create(self, 
                login: str, 
                name: str, 
                organisation: str, 
                profile: str, 
                password: str,
                email: str = "", 
            ) -> UserResponce:
        
        
        
        json = {
            "login": login,
            "name": name,
            "organisation": organisation,
            "profile": profile,
            "email": email,
            "password": password
        }
        
        try:
            self.get(login)
        except:
            return self._post("api/v1/user", json, UserResponce)
        else:
            raise HiveException("User already exist")
    
    def set_password(self, id: str, password: str) -> UserResponce:
        json = {
            "password": password
        }
        
        responce = self._post(f"api/v1/user/{id}/password/set", json, UserResponce)

        return responce
    
    def generate_api(self, id: str) -> tuple[str, UserResponce]:
        json ={}
        responce = self._post(f"api/v1/user/{id}/key/renew", json, UserResponce)
        responce.content: bytes
        
        return responce.content.decode("utf-8"), responce
    
    def revoke_api(self, id: str) -> UserResponce:
        responce = self._delete(f"api/v1/user/{id}/key", UserResponce)
        
        return responce
    
    def get_api(self, id: str) -> tuple[str, UserResponce]:
        responce = self._get(f"api/v1/user/{id}/key", UserResponce)
        responce.content: bytes
        
        return responce.content.decode("utf-8"), responce

    def lock(self, id: str, flag: bool) -> UserResponce:
        json = {
            "locked": flag   
        }
        
        return self._patch(f"api/v1/user/{id}", json, UserResponce)
    
    def delete(self, id: str, organisation: str) -> UserResponce:
        return self._delete(f"api/v1/user/{id}/force?organisation={organisation}", UserResponce)
        