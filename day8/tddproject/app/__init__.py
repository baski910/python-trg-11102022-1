import os
from flask_api import FlaskAPI
from flask import request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
#from .models import Book

db = SQLAlchemy()

def create_app():
    from app.models import Book
    app = FlaskAPI(__name__, instance_path=os.getcwd(),instance_relative_config= True)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
    db.init_app(app)
    
    @app.route('/booklists',methods=['POST','GET'])
    def booklists():
        if request.method == 'POST':
            name = str(request.data.get('name',''))
            if name:
                booklist = Book(name=name)
                booklist.save()
                response = jsonify(
                    {
                        'id': booklist.id,
                        'name': booklist.name,
                    }
                )
                response.status_code = 201
                return response
        else:
            booklists = Book.get_all()
            results = []
            for booklist in booklists:
                obj = {
                    'id': booklist.id,
                    'name': booklist.name,
                    
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response
    
    return app