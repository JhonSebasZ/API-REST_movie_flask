class Review:
    def __init__(self, name, email, description, rating, code_movie, id=None) -> None:
        self.__name = name
        self.__email = email
        self.__description = description
        self.__rating = rating
        self.__code_movie = code_movie
        self.__id = id
    
    def getName(self) -> str:
        return self.__name
    
    def getEmail(self) -> str:
        return self.__email
    
    def getDescription(self) -> str:
        return self.__description
    
    def getRating(self) -> int:
        return self.__rating
    
    def getCodeMovie(self) -> str:
        return self.__code_movie
    
    def getId(self) -> int:
        return self.__id
    
    def toDic(self):
        return {
            'name': self.__name,
            'email': self.__email,
            'description': self.__description,
            'rating': self.__rating,
            'code_movie': self.__code_movie
        }