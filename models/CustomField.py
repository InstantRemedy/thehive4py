from .AbstractModel import *

class CustomField(AbstractModel):
    def __init__(self, json: dict) -> None:
        super().__init__(json)
        
    @property
    def id(self) -> str:
        return self.json["id"]
    
    @property
    def name(self) -> str:
        return self.json["name"]

    @property
    def reference(self) -> str:
        return self.json["reference"]
    
    @property
    def description(self) -> str:
        return self.json["description"]
    
    @property
    def type(self) -> str:
        return self.json["type"]

    @property
    def mandatory(self) -> bool:
        return self.json["mandatory"]
    
    @property
    def options(self) -> list[str]:
        return self.json["options"]