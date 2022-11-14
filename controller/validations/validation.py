from controller.response.api import ApiResponse
class Validation:
    def required(self, validation, name) -> ApiResponse:
        if validation is None:
            api = ApiResponse(message=f'The {name} of the movie is required')
            return api.toDic()
    
    def isStr(self, validation, name) -> ApiResponse:
        if validation is None:
            return
        if not isinstance(validation,str):
            api = ApiResponse(message=f'The {name} mush be a string')
            return api.toDic()

    
    def isInt(self, validation, name) -> ApiResponse:
        if validation is None:
            return
        if not isinstance(validation, int):
            api = ApiResponse(message=f'The {name} mush be a int')
            return api.toDic()
        