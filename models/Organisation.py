from .AbstractModel import AbstractModel as _AbstractModel

class Organisation(_AbstractModel):
    def __init__(self, json : dict):
        super().__init__(json)
    
    @property
    def id(self) -> str:
        return self.json["id"]
    
    @property
    def m_type(self) -> str:
        return self.json["_type"]
    
    @property
    def created_by(self) -> str:
        return self.json["createdBy"]
    
    @property
    def created_at(self) -> str:
        return self.json["createdAt"]
    
    @property
    def name(self) -> str:
        return self.json["name"]
    
    @property
    def description(self) -> str:
        return self.json["description"]
    
    @property
    def links(self) -> list[str]:
        return self.json["links"]
    
    @property
    def m_id(self) -> str:
        return self.json["_id"]