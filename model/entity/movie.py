class Movie:
    def __init__(self, code, name, image_url=None, year=None) -> None:
        self.__code = code
        self.__name = name
        self.__image_url = image_url
        self.__year = year
    
    def getCode(self) -> str:
        return self.__code
    
    def getName(self) -> str:
        return self.__name
        
    def getImageUrl(self) -> str:
        return self.__image_url
    
    def setImageUrl(self, image_url:str) -> None:
        self.__image_url = image_url
        
    def getYear(self) -> int:
        return self.__year
    
    def setYear(self, year:int) -> None:
        self.__year = year
    
    def toDic(self):
        return {
            'code': self.__code,
            'name': self.__name,
            'image_url': self.__image_url,
            'year': self.__year
        }