import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.review.models import Review
 
catalog = Blueprint('catalog', __name__)
 
@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the Catalog Home."
 
 
class ReviewView(MethodView):
 
    def get(self, id=None, page=1):
        if not id:
            reviews = Review.query.paginate(page, 10).items
            res = {}
            for review in reviews:
                res[review.id] = {
                    'title': review.title,
                    'rating': str(review.rating),
                    'body': review.body,
                }
        else:
            review = Review.query.filter_by(id=id).first()
            if not review:
                abort(404)
            res = {
                'title': review.title,
                'rating': str(review.rating),
                'body': review.body,
            }
        return jsonify(res)
 
    def post(self):
        title = request.form.get('title')
        rating = request.form.get('rating')
        body = request.form.get('body')
        review = Review(title, rating, body)
        db.session.add(review)
        db.session.commit()
        return jsonify({review.id: {
            'title': review.title,
            'rating': str(review.rating),
            'body': review.body,
        }})
 
    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return
 
    def delete(self, id):
        # Delete the record for the provided id.
        return
 
 
review_view =  ReviewView.as_view('review_view')
app.add_url_rule(
    '/review/', view_func=review_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/review/<int:id>', view_func=review_view, methods=['GET']
)