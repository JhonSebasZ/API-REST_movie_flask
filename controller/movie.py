from application import app
from model.entity.movie import Movie
from model.repository.movie import MovieRepository
from flask import request
from controller.response.api import ApiResponse
from MySQLdb import IntegrityError

repository = MovieRepository()

@app.route('/api/movies', methods=['GET'])
def listMovies():
    response = repository.findAll()
    movies = [movie.toDic() for movie in response]
    api = ApiResponse(data=movies)
    return api.toDic(), 200

@app.route('/api/movies/<code>', methods=['GET'])
def listMoviesByCode(code):
    api = None
    status = 400
    try:
        movie = repository.findByCode(code)
        api = ApiResponse(data=movie.toDic())
        status = 200
    except Exception as ex:
        api = ApiResponse(message=str(ex))
        return api.toDic(), status
    return api.toDic(), status

@app.route('/api/movies', methods=['POST'])
def create():
    status = 400
    data = request.get_json(force=True)
    
    if data.get('code') is None:
        api = ApiResponse(message='The code of the movie is required')
        return api.toDic(), status
    
    if data.get('name') is None:
        api = ApiResponse(message='The name of the movie is required')
        return api.toDic(), status
        
    movie = Movie(
        code=data.get('code'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        year=data.get('year')
    )
    
    try:
        repository.insert(movie)
    except IntegrityError as ex:
        if ex.args[0] != 1062:
            api = ApiResponse(message=str(ex))
            return api.toDic()
        
        api = ApiResponse(message='The movie already exists')
        return api.toDic(), status
    except:
        api = ApiResponse(message='Unexpeted error')
        return api.toDic(), status
        
    api = ApiResponse(data=True)
    status = 201
    return api.toDic(), status
