from .AbstractModel import AbstractModel as _AbstractModel

class User(_AbstractModel):
    def __init__(self, json: dict) -> None:
        super().__init__(json)

    def __str__(self):
        return f"User({self.login})"
    
    @property
    def m_id(self) -> str:
        return self.json["_id"]
    
    @property
    def m_created_by(self) -> str:
        return self.json["_createdBy"]
    
    @property
    def m_created_at(self) -> str:
        return self.json["_createdAt"]
    
    @property
    def login(self) -> str:
        return self.json["login"]
    
    @property
    def name(self) -> str:
        return self.json["name"]
    
    @property
    def has_key(self) -> bool:
        return self.json["hasKey"]
    
    @property
    def has_password(self) -> bool:
        return self.json["hasPassword"]
    
    @property
    def has_MFA(self) -> bool:
        return self.json["hasMFA"]
    
    @property
    def locked(self) -> bool:
        return self.json["locked"]
    
    @property 
    def profile(self) -> str:
        return self.json["profile"]
    
    @property
    def permissions(self) -> list[str]:
        return self.json["permissions"]
    
    @property
    def organisation(self) -> str:
        return self.json["organisation"]
    
    @property
    def organisations(self) -> list[str]:
        return self.json["organisations"]
    
    @property
    def email(self) -> str:
        return self.json["email"]