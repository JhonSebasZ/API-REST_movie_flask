from model.entity.movie import Movie
from model.connection_db import execute, commit

class MovieRepository():
    def insert(movie:Movie) -> None:
        sql = f"""
                INSERT INTO movie (code, name, image_url, year)
                VALUES ('{movie.get_code()}', '{movie.get_name()}',
                        '{movie.get_image_url()}', '{movie.get_year()}')
            """
        cursor = execute(sql)
        cursor.close()
        commit()   
    
    def find_by_code(code:str) -> Movie:
        sql = f"""
                SELECT * FROM movie
                WHERE code='{code}'
            """
        cursor = execute(sql)
        result = cursor.fetchone()
        cursor.close()
        movie = Movie(
            code=result[0], name=result[1],
            image_url=result[2], year=result[3]
        )
        
        return movie
    
    def find_all() -> list:
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
