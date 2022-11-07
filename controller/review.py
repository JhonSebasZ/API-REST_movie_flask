from aplication import app
from model.entity.review import Review
from model.repository.review import ReviewRepository

repositoty = ReviewRepository()

@app.route('/api/reviews/', methods=['POST'])
def create():
    review = Review()
    repositoty.insert(review)

@app.route('/api/reviews/<id>', methods=['GET'])
def find_by_id(id):
    return repositoty.find_by_id(id)

@app.route('/api/reviews/<code>', methods=['GET'])
def find_by_movie_code(code):
    return repositoty.find_by_movie_code(code)

@app.route('/api/reviews', methods=['PUT'])
def update():
    review = Review()
    repositoty.update(review)

@app.route('/api/reviews/<id>')
def delete(id):
    repositoty.delete(id)
