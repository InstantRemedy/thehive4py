from .AbstractResponce import AbstractResponce as _AbstractResponce
import requests as _requests

class CustomFieldResponce(_AbstractResponce):
    def __init__(self, responce: _requests.Response) -> None:
        super().__init__(responce)
        
    @property
    def id(self) -> str:
        return self._get_value("id")
    
    @property
    def name(self) -> str:
        return self._get_value("name")
    
    @property
    def reference(self) -> str:
        return self._get_value("reference")
    
    @property
    def description(self) -> str:
        return self._get_value("description")
    
    @property
    def type(self) -> str:
        return self._get_value("type")
    
    @property
    def mandatory(self) -> bool:
        return self._get_value("mandatory")
    
    @property
    def options(self) -> list[str]:
        return self._get_value("options")