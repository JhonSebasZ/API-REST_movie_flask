from application import app
from model.entity.review import Review
from model.repository.review import ReviewRepository
from controller.response.api import ApiResponse
from controller.validations.validation import Validation
from flask import request

repository = ReviewRepository()

@app.route('/api/reviews', methods=['POST'])
def createReview():
    validation = Validation()
    status = 400
    data = request.get_json(force=True)
    # validaciones
    if validation.required(data.get('name'), 'name'):
        return validation.required(data.get('name'), 'name'), status
    if validation.required(data.get('email'), 'email'):
        return validation.required(data.get('email'), 'email'), status
    if validation.required(data.get('description'), 'description'):
        return validation.required(data.get('description'), 'description'), status
    if validation.required(data.get('rating'), 'rating'):
        return validation.required(data.get('rating'), 'rating'), status
    if validation.required(data.get('code'), 'code'):
        return validation.required(data.get('code'), 'code'), status
    
    if validation.isStr(data.get('name'), 'name'):
        return validation.isStr(data.get('name'), 'name'), status
    if validation.isStr(data.get('email'), 'email'):
        return validation.isStr(data.get('email'), 'email'), status
    if validation.isStr(data.get('description'), 'description'):
        return validation.isStr(data.get('description'), 'description'), status
    if validation.isInt(data.get('rating'), 'rating'):
        return validation.isInt(data.get('rating'), 'rating'), status
    if validation.isStr(data.get('code'), 'code'):
        return validation.isStr(data.get('code'), 'code'), status
    
    review = Review(
        name=data.get('name'),
        email=data.get('email'),
        description=data.get('description'),
        rating=data.get('rating'),
        code_movie=data.get('code') 
    )
    try:
        repository.create(review)
        api = ApiResponse(data=True)
        status = 201
    except Exception as ex:
        api = ApiResponse(message=str(ex))
    return api.toDic(), status
    
@app.route('/api/reviews/<id>', methods=['GET'])
def findReviewById(id):
    try:
        review = repository.findById(id)
        api = ApiResponse(data=review.toDic())
        return api.toDic(), 200
    except Exception as ex:
        api = ApiResponse(message=str(ex))
        return api.toDic(), 400
    
@app.route('/api/reviews/movie/<code>', methods=['GET'])
def findReviewByMovieCode(code):
    api = None
    status = 200
    try:
        response = repository.findByMovieCode(code)
        reviews = [review.toDic() for review in response]
        if len(reviews) == 0:
            status = 204
        api = ApiResponse(data=reviews)
    except Exception as ex:
        api = ApiResponse(message=str(ex))
        status = 400
    return api.toDic(), status

@app.route('/api/reviews/<id>', methods=['PUT'])
def update(id):
    validation = Validation()
    data = request.get_json(force=True)
    status = 400
    
    # validaciones
    if validation.required(data.get('name'), 'name'):
        return validation.required(data.get('name'), 'name'), status
    if validation.required(data.get('email'), 'email'):
        return validation.required(data.get('email'), 'email'), status
    if validation.required(data.get('description'), 'description'):
        return validation.required(data.get('description'), 'description'), status
    if validation.required(data.get('rating'), 'rating'):
        return validation.required(data.get('rating'), 'rating'), status
    if validation.required(data.get('code'), 'code'):
        return validation.required(data.get('code'), 'code'), status
    
    if validation.isStr(data.get('name'), 'name'):
        return validation.isStr(data.get('name'), 'name'), status
    if validation.isStr(data.get('email'), 'email'):
        return validation.isStr(data.get('email'), 'email'), status
    if validation.isStr(data.get('description'), 'description'):
        return validation.isStr(data.get('description'), 'description'), status
    if validation.isInt(data.get('rating'), 'rating'):
        return validation.isInt(data.get('rating'), 'rating'), status
    if validation.isStr(data.get('code'), 'code'):
        return validation.isStr(data.get('code'), 'code'), status
    
    review = Review(
        id = id,
        name=data.get('name'),
        email=data.get('email'),
        description=data.get('description'),
        rating=data.get('rating'),
        code_movie=data.get('code') 
    )
    try:
        repository.update(review)
        api = ApiResponse(data=True)
        status = 200
    except Exception as ex:
        api = ApiResponse(message=str(ex))
        status = 209
    return api.toDic(), status

@app.route('/api/reviews/<id>', methods=['DELETE'])
def delete(id):
    api = None
    status = 200
    try:
        # TODO: Validar campos
        repository.delete(id)
        api = ApiResponse(data=True)
    except Exception as ex:
        api = ApiResponse(message=str(ex))
        status = 409
    return api.toDic(), status
