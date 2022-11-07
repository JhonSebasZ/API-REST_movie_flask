from model.entity.review import Review
from model.connection_db import execute, commit

class ReviewRepository:
    def insert(review:Review) -> None:
        sql = f"""
                INSERT INTO review (name, email, description, rating, code)
                VALUE ('{review.get_name()}', '{review.get_email()}',
                '{review.get_description()}', {review.get_rating()}, '{review.get_code()}')
            """
        cursor = execute(sql)
        cursor.close()
        commit()
    
    def find_by_id(id:int) -> Review:
        sql = f"""
                SELECT * FROM review 
                WHERE id={id}
            """
        cursor = execute(sql)
        result = cursor.fetchone()
        cursor.close()
        review = Review(id=result[0], name=result[1], email=result[2],
                        description=result[3], rating=result[4], code_movie=result[5])

        return review
        
    def find_by_movie_code(code:str) -> list:
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
    
    def update(review:Review) -> None:
        sql = f"""
                UPDATE review
                SET name='{review.get_name()}',
                    email='{review.get_email()}',
                    description='{review.get_description()}',
                    rating='{review.get_rating()}',
                    code='{review.get_code_movie()}'
                WHERE id={review.get_id()}
            """
        cursor = execute(sql)
        cursor.close()
        commit()
    
    def delete(id:int) -> None:
        sql = f"""
                DELETE FROM review
                WHERE id={id}
            """
        
        cursor = execute(sql)
        cursor.close()
        commit()