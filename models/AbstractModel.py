import abc as _abc

class AbstractModel(_abc.ABC):
    def __init__(self, json : dict) -> None:
        super().__init__()
        self.__json : dict = json
    
    def __str__(self) -> str:
        return self.__json.__str__()
    
    @property
    def json(self) -> dict:
        return self.__json
