from model.entity.review import Review
from model.connection_db import execute, commit

class ReviewRepository:
    def create(self, review:Review) -> None:
        sql = f"""
                INSERT INTO review (name, email, description, rating, code)
                VALUE ('{review.getName()}', '{review.getEmail()}',
                '{review.getDescription()}', {review.getRating()}, '{review.getCodeMovie()}')
            """
        cursor = execute(sql)
        cursor.close()
        commit()
    
    def findById(self, id:int) -> Review:
        sql = f"""
                SELECT * FROM review 
                WHERE id={id}
            """
        cursor = execute(sql)
        result = cursor.fetchone()
        cursor.close()
        
        if result == None:
            raise Exception(f'The movie with the code "{id}" does not exist')
        
        review = Review(id=result[0], name=result[1], email=result[2],
                        description=result[3], rating=result[4], code_movie=result[5])
        
        return review
        
    def findByMovieCode(self, code:str) -> list:
        sql = f"""
                SELECT * FROM review
                WHERE code='{code}'
            """
        cursor = execute(sql)
        results = cursor.fetchall()
        cursor.close()
        
        reviews = list()
        for review in results:
            reviews.append(
                Review(id=review[0], name=review[1], email=review[2],
                    description=review[3], rating=review[4], code_movie=review[5])
            )
        
        return reviews
    
    def update(self, review:Review) -> None:
        sql = f"""
                UPDATE review
                SET name='{review.getName()}',
                    email='{review.getEmail()}',
                    description='{review.getDescription()}',
                    rating='{review.getRating()}',
                    code='{review.getCodeMovie()}'
                WHERE id={review.getId()}
            """
        cursor = execute(sql)
        cursor.close()
        commit()
    
    def delete(self, id:int) -> None:
        sql = f"""
                DELETE FROM review
                WHERE id={id}
            """
        
        cursor = execute(sql)
        cursor.close()
        commit()