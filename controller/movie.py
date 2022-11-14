from application import app
from model.entity.movie import Movie
from model.repository.movie import MovieRepository
from flask import request
from controller.response.api import ApiResponse
from MySQLdb import IntegrityError
from controller.validations.validation import Validation

repository = MovieRepository()

@app.route('/api/movies', methods=['GET'])
def listMovies():
    try:
        response = repository.findAll()
        movies = [movie.toDic() for movie in response]
        api = ApiResponse(data=movies)
        return api.toDic(), 200
    except Exception as ex:
        api = ApiResponse(message=str(ex))
        return api.toDic(), 400

@app.route('/api/movies/<code>', methods=['GET'])
def listMoviesByCode(code):
    api = None
    status = 400
    try:
        movie = repository.findByCode(code)
        api = ApiResponse(data=movie.toDic())
        status = 200
        return api.toDic(), status
    except Exception as ex:
        api = ApiResponse(message=str(ex))
        return api.toDic(), status

@app.route('/api/movies', methods=['POST'])
def create():
    status = 400
    data = request.get_json(force=True)
    validation = Validation()
    
    # Mandatory data validation
    if validation.required(data.get('code'), 'code'):
        return validation.required(data.get('code'), 'code'), status
    if validation.required(data.get('name'), 'name'):
        return validation.required(data.get('name'), 'name'), status
    
    # Data type validations
    if validation.isStr(data.get('code'), 'code'):
        return validation.isStr(data.get('code'), 'code'), status
    if validation.isStr(data.get('name'), 'name'):
        return validation.isStr(data.get('name'), 'name'), status
    if validation.isStr(data.get('image_url'), 'image_url'):
        return validation.isStr(data.get('image_url'), 'image_url'), status
    if validation.isInt(data.get('year'), 'year'):
        return validation.isInt(data.get('year'), 'year'), status               
        
    movie = Movie(
        code=data.get('code'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        year=data.get('year')
    )
    
    #exception handling
    try:
        repository.create(movie)
        api = ApiResponse(data=True)
        status = 201
        return api.toDic(), status
    except IntegrityError as ex:
        if ex.args[0] != 1062:
            api = ApiResponse(message=str(ex))
            return api.toDic()
        
        api = ApiResponse(message='The movie already exists')
        return api.toDic(), status
    except:
        api = ApiResponse(message='Unexpeted error')
        return api.toDic(), status
