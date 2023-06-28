from ..exceptions.HiveException import *
from ..responces.LoginResponce import *
from .AbstractRequest import *
from ..utils.utils import *

import requests

class LoginRequest(AbstractRequest):
    def __init__(self, session: requests.Session, url: str):
        super().__init__(session, url)
    
    def login(self, user: str, password: str) -> LoginResponce:
        
        json = {
            "user": user,
            "password": password
        }
            
        return self._post("api/login", json, LoginResponce)