import abc as _abc
import requests as _requests

class AbstractResponce(_abc.ABC, _requests.Response):
    def __init__(self, responce: _requests.Response) -> None:
        super().__init__()
        self.url = responce.url
        self.status_code = responce.status_code 
        self.reason = responce.reason 
        self.headers = responce.headers 
        self.elapsed = responce.elapsed 
        self.request = responce.request

        if "Content-Type" in responce.headers:
            if responce.headers["Content-Type"] == "application/json":
                self.__content = responce.json()
                
            elif responce.headers["Content-Type"] == "text/plain":
                self.__content = responce.text
            else:
                self.__content = responce.content
        else:
            self.__content = None
    
    def __str__(self) -> str:
        return self.content.__str__()
    
    def _get_value(self, key: str = "") -> dict | list | bytes | None:
        if type(self.content) == dict:
            if key == "":
                raise ValueError("key must be not empty")
            keys  = [key, "_" + key]
            for key in keys:
                if key in self.content:
                    return self.content[key]
            raise KeyError(f"key: {key} not found")
        elif type(self.content) == list or bytes:
            return self.content
        else:
            raise TypeError("content must be dict, list or bytes")

    @property
    def content(self) -> dict | list | bytes | None:
        return self.__content