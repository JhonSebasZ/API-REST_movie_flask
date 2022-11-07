from aplication import app
from model.entity.movie import Movie
from model.repository.movie import MovieRepository

repository = MovieRepository()

@app.route('/api/movies', methods=['GET'])
def list():
    return repository.find_all()

@app.route('/api/movies/<code>', methods=['GET'])
def list_by_code(code):
    return repository.find_by_code(code)

@app.route('/api/movies', methods=['POST'])
def create():
    movie = Movie()
    repository.insert(movie)
