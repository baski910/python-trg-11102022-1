import os
from flask import Flask, render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    from .models import Book
    app = Flask(__name__,instance_path=os.getcwd(),instance_relative_config=True)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate = Migrate(app,db)

    @app.route('/')
    def index():
        books = []
        records = Book.query.all()
        for record in records:
            books.append({'title': record.title, 'author': record.author})
        return render_template('home.html', books = books)

    @app.route('/addbooks', methods=['GET','POST'])
    def addbooks():
        if request.method == "POST":
            title = request.form['title']
            author = request.form['author']
            book = Book(title=title,author=author)
            db.session.add(book)
            db.session.commit()
        #msg = "Successfully added book"
        return redirect(url_for('index'))
        #return render_template("home.html",message=msg)

    return app
