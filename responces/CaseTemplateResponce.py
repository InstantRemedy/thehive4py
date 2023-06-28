from .AbstractResponce import AbstractResponce as _AbstractResponce
import requests as _requests

class CaseTemplateResponce(_AbstractResponce):
    def __init__(self, responce: _requests.Response) -> None:
        super().__init__(responce)
    
    @property
    def id(self) -> str:
        return self._get_value("id")
    
    @property
    def type(self) -> str:
        return self._get_value("type")

    @property
    def created_by(self) -> str:
        return self._get_value("createdBy")
    
    @property
    def updated_by(self) -> str:
        return self._get_value("updatedBy")
    
    @property
    def created_at(self) -> str:
        return self._get_value("createdAt")
    
    @property
    def updated_at(self) -> str:
        return self._get_value("updatedAt")
    
    @property
    def name(self) -> str:
        return self._get_value("name")
    
    @property
    def display_name(self) -> str:
        return self._get_value("displayName")
    
    @property
    def title_prefix(self) -> str:
        return self._get_value("titlePrefix")
    
    @property
    def description(self) -> str:
        return self._get_value("description")
    
    @property
    def severity(self) -> int:
        return self._get_value("severity")
    
    @property
    def tags(self) -> list[str]:
        return self._get_value("tags")
    
    @property
    def flag(self) -> bool:
        return self._get_value("flag")
    
    @property
    def tlp(self) -> int:
        return self._get_value("tlp")
    
    @property
    def pap(self) -> int:
        return self._get_value("pap")
    
    @property
    def custom_fields(self) -> list:
        return self._get_value("customFields")
    
    @property
    def tasks(self) -> list:
        return self._get_value("tasks")
    
    @property
    def status(self) -> str:
        return self._get_value("status")
    
    @property
    def metrics(self) -> dict:
        return self._get_value("metrics")