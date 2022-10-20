from app import mw
from .models import Book

class BookSchema(mw.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
