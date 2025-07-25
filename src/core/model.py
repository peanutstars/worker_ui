import json


class ApiResponse:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

    def data(self):
        return self.__dict__


class ApiRequestResponse(ApiResponse):
    success = False
    value = {}
    message = ""
    command = ""
