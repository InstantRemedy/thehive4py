from .AbstractResponce import *
import requests as _requests

class UserResponce(AbstractResponce):
    def __init__(self, responce: _requests.Response) -> None:
        super().__init__(responce)
    
    @property
    def id(self) -> str:
        return self._get_value("id")
    
    @property
    def created_by(self) -> str:
        return self._get_value("createdBy")

    @property
    def created_at(self) -> str:
        return self._get_value("createdAt")

    @property
    def login(self) -> str:
        return self._get_value("login")
    
    @property
    def name(self) -> str:
        return self._get_value("name")
    
    @property
    def has_key(self) -> bool:
        return self._get_value("hasKey")
    
    @property
    def has_password(self) -> bool:
        return self._get_value("hasPassword")
    
    @property
    def has_MFA(self) -> bool:
        return self._get_value("hasMFA")
    
    @property
    def locked(self) -> bool:
        return self._get_value("locked")
    
    @property
    def profile(self) -> dict:
        return self._get_value("profile")
    
    @property
    def permissions(self) -> list[str]:
        return self._get_value("permissions")
    
    @property
    def organisation(self) -> str:
        return self._get_value("organisation")
    
    @property
    def organisations(self) -> list[str]:
        return self._get_value("organisations")
    
    @property
    def email(self) -> str:
        return self._get_value("email")