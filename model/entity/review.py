class Review:
    def __init__(self, name, email, description, rating, code_movie, id=None) -> None:
        self.__name = name
        self.__email = email
        self.__description = description
        self.__rating = rating
        self.__code_movie = code_movie
        self.__id = id
    
    def get_name(self) -> str:
        return self.__name
    
    def get_email(self) -> str:
        return self.__email
    
    def get_description(self) -> str:
        return self.__description
    
    def get_rating(self) -> int:
        return self.__rating
    
    def get_code_movie(self) -> str:
        return self.__code_movie
    
    def get_id(self) -> int:
        return self.__id