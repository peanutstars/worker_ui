import json


class ApiRequestResponse:
    success = False
    value = {}
    message = ""
    request = ""
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
    
    def data(self):
        return self.__dict__