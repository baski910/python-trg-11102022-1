import os
from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mw = Marshmallow()


def create_app():
    from .models import Book
    from .schemas import BookSchema
    from .resources import BookListResource
    app = Flask(__name__,instance_path=os.getcwd(),instance_relative_config=True)
    app.config.from_pyfile('config.py')
    api = Api(app)

    db.init_app(app)
    mw.init_app(app)
    migrate = Migrate(app,db)
    
    
    api.add_resource(BookListResource, "/books")

    return app
