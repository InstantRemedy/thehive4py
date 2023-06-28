import abc

class HiveException(abc.ABC, BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
        self.__json = {}
        
        for arg in args:
            if isinstance(arg, dict):
                self.__json = arg
    
    @property
    def type(self) -> str:
        return self.__json["type"]
    
    @property
    def message(self) -> str:
        return self.__json["message"]
        
    def __str__(self) -> str:
        if self.__json != {}:
            return f"\n\n[TYPE]:{self.type}\n[MESSAGE]:{self.message}\n[JSON]:{self.__json}"
        else:
            return super().__str__()
    
    