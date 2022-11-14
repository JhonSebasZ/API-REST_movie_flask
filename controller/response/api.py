class ApiResponse:
    def __init__(self, data=None, message=None) -> None:
        self.__data = data
        self.__message = message
        
    def toDic(self):
        return {
            'data': self.__data,
            'error': self.__message !=None,
            'message': self.__message
        }