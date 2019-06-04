from my_app import db
 
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    rating = db.Column(db.Integer())
    body = db.Column(db.String(1000))
 
    def __init__(self, title, rating, body):
        self.title = title
        self.rating = rating
        self.body = body
 
    def __repr__(self):
        return '<Review %d>' % self.id