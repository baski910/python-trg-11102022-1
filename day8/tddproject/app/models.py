from app import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    #date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self,name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Book.query.all()

    def __repr__(self):
        return "<Book: {}>".format(self.name)
