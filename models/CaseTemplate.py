from .AbstractModel import *

class CaseTemplate(AbstractModel):
    def __init__(self, json: dict) -> None:
        super().__init__(json)
        
    @property
    def m_id(self) -> str:
        return self.json["_id"]
    
    @property
    def m_type(self) -> str:
        return self.json["_type"]
    
    @property
    def m_created_by(self) -> str:
        return self.json["_createdBy"]
    
    @property
    def m_updated_by(self) -> str:
        return self.json["_updatedBy"]
    
    @property
    def m_created_at(self) -> int:
        return self.json["_createdAt"]
    
    @property
    def m_updated_at(self) -> int:
        return self.json["_updatedAt"]
    
    @property
    def name(self) -> str:
        return self.json["name"]
    
    @property
    def display_name(self) -> str:
        return self.json["displayName"]
    
    @property
    def title_prefix(self) -> str:
        return self.json["titlePrefix"]
    
    @property
    def description(self) -> str:
        return self.json["description"]
    
    @property
    def severity(self) -> int:
        return self.json["severity"]
    
    @property
    def tags(self) -> list[str]:
        return self.json["tags"]
    
    @property
    def flag(self) -> bool:
        return self.json["flag"]
    
    @property
    def tlp(self) -> int:
        return self.json["tlp"]
    
    @property
    def pap(self) -> int:
        return self.json["pap"]
    
    @property
    def custom_fields(self) -> dict:
        return self.json["customFields"]
    
    @property
    def tasks(self) -> list[dict]:
        return self.json["tasks"]