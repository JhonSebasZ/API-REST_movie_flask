from model.entity.movie import Movie
from model.connection_db import execute, commit

class MovieRepository():
    def create(self,movie:Movie) -> None:
        image = movie.getImageUrl() if movie.getImageUrl() != None else 'NULL'
        year = movie.getYear() if movie.getYear() != None else 'NULL'
        sql = f"""
                INSERT INTO movie (code, name, image_url, year)
                VALUES ('{movie.getCode()}', '{movie.getName()}',
                        '{image}', {year})
            """
        cursor = execute(sql)
        cursor.close()
        commit()   
    
    def findByCode(self, code:str) -> Movie:
        sql = f"""
                SELECT * FROM movie
                WHERE code='{code}'
            """
        cursor = execute(sql)
        result = cursor.fetchone()
        cursor.close()
        
        if result == None:
            raise Exception(f'The movie with the code "{code}" does not exist')
        
        movie = Movie(
            code=result[0], name=result[1],
            image_url=result[2], year=result[3]
        )
        
        return movie
    
    def findAll(self) -> list:
        sql = """
                SELECT * FROM movie
            """
        cursor = execute(sql)
        results = cursor.fetchall()
        cursor.close()
        
        movies = list()
        for movie in results:
            movies.append(
                Movie(code=movie[0], name=movie[1],
                    image_url=movie[2], year=movie[3]
                )
            )
        return movies
