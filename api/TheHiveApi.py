from ..models.Organisation import *
from ..models.User import *

from ..responces.OrganisationResponce import *
from ..responces.LoginResponce import *
from ..responces.UserResponce import *
from ..responces.CustomFieldResponce import *
from ..responces.CaseTemplateResponce import *

from ..requests.LoginRequest import *
from ..requests.OrganisationRequest import *
from ..requests.UserRequest import *
from ..requests.CustomFieldRequest import *
from ..requests.CaseTemplateRequest import *

from ..utils import utils as _utils

import requests as _requests

class TheHiveApi(object):
    def __init__(self, 
                 ip : str, 
                 port : int) -> None:
        
        _utils.check_type((ip, str), (port, int))
        
        self.__session = _requests.Session()
        self.__url = f"http://{ip}:{port}/"
        self.__login_request = LoginRequest(self.__session, self.__url)
        self.__organisation_request = OrganisationRequest(self.__session, self.__url)
        self.__user_request = UserRequest(self.__session, self.__url)
        self.__customField_request = CustomFieldRequest(self.__session, self.__url)
        self.__case_template_request = CaseTemplateRequest(self.__session, self.__url)
        
    @property
    def login_request(self) -> LoginRequest:
        return self.__login_request
    
    @property
    def organisation_request(self) -> OrganisationRequest:
        return self.__organisation_request

    @property
    def user_request(self) -> UserRequest:
        return self.__user_request
    
    @property
    def custom_field_request(self) -> CustomFieldRequest:
        return self.__customField_request
    
    @property
    def case_template_request(self) -> CaseTemplateRequest:
        return self.__case_template_request
    
    def check_status(self) -> _requests.Response:
        req = self.__session.get(self.__url + "api/status")
        return req
    
        
    def __str__(self) -> str:
        return f"TheHiveApi({self.__url})"