from .AbstractResponce import AbstractResponce as _AbstractResponce
import requests as _requests

class LoginResponce(_AbstractResponce):
    def __init__(self, responce: _requests.Response) -> None:
        super().__init__(responce)
    
    @property
    def id(self) -> str:
        return self._get_value("id")
    
    @property
    def created_by(self) -> str:
        return self._get_value("createdBy")
    
    @property
    def updated_by(self) -> str:
        return self._get_value("updatedBy")
    
    @property
    def created_at(self) -> int:
        return self._get_value("createdAt")
    
    @property
    def updated_at(self) -> int:
        return self._get_value("updatedAt")
    
    @property
    def m_type(self) -> str:
        return self._get_value("_type")
    
    @property
    def logi(self) -> str:
        return self._get_value("login")
    
    @property
    def name(self) -> str:
        return self._get_value("name")
    
    @property
    def roles(self) -> list:
        return self._get_value("roles")
    
    @property
    def organisation(self) -> str:
        return self._get_value("organisation")
    
    @property
    def has_key(self) -> bool:
        return self._get_value("hasKey")
    
    @property
    def status(self) -> str:
        return self._get_value("status")