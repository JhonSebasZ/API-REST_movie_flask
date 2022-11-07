class Movie:
    def __init__(self, code, name, image_url=None, year=None) -> None:
        self.__code = code
        self.__name = name
        self.__image_url = image_url
        self.__year = year
    
    def get_code(self) -> str:
        return self.__code
    
    def get_name(self) -> str:
        return self.__name
        
    def get_image_url(self) -> str:
        return self.__image_url
    
    def set_image_url(self, image_url:str) -> None:
        self.__image_url = image_url
        
    def get_year(self) -> int:
        return self.__year
    
    def set_year(self, year:int) -> None:
        self.__year = year