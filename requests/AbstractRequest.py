from ..exceptions.HiveException import *
from ..responces.AbstractResponce import *

import abc
import requests

class AbstractRequest(abc.ABC):
    def __init__(self, session: requests.Session, url: str):
        self.__session = session
        self.__url = url

    def _get(self, endpoint: str, responce: type[AbstractResponce]) -> AbstractResponce:
        res = self.__session.get(self.__url + endpoint)
        
        if(res.status_code >= 400):
            raise HiveException(res.json())
        
        return responce(res)

    def _post(self, endpoint: str, json: dict, responce: type[AbstractResponce]) -> AbstractResponce:
        res = self.__session.post(self.__url + endpoint, json=json)
        
        if(res.status_code >= 400):
            raise HiveException(res.json())
        
        return responce(res)
    
    def _patch(self, endpoint: str, json: dict, responce: type[AbstractResponce]) -> AbstractResponce:
        res = self.__session.patch(self.__url + endpoint, json=json)
        
        if(res.status_code >= 400):
            raise HiveException(res.json())
        
        return responce(res)
    
    def _delete(self, endpoint: str, responce: type[AbstractResponce] = None) -> AbstractResponce | requests.Response:
        res = self.__session.delete(self.__url + endpoint)
        
        if(res.status_code >= 400):
            raise HiveException(res.json())
        
        responce = responce(res) if responce != None else res
        
        return responce