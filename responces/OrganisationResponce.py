from .AbstractResponce import AbstractResponce as _AbstractResponce
import requests as _requests

class OrganisationResponce(_AbstractResponce):
    def __init__(self, responce: _requests.Response) -> None:
        super().__init__(responce)
    
    @property
    def name(self) -> str:
        return self._get_value("name")
    
    @property
    def description(self) -> str:
        return self._get_value("description")

    @property
    def id(self) -> str:
        return self._get_value("id")
    
    @property
    def created_at(self) -> int:
        return self._get_value("createdAt")
    
    @property
    def created_by(self) -> str:
        return self._get_value("createdBy")

    @property
    def m_type(self) -> str:
        return self._get_value("_type")
    
    @property
    def links(self) -> list:
        return self._get_value("links")
    
