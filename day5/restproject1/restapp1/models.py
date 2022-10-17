from django.db import models

# Create your models here.
class Book(models.Model):
    booktitle = models.CharField(max_length=50)
    bookauthor = models.CharField(max_length=50)
    class Meta:
        db_table = 'books'

    def __repr__(self):
        return f"{self.booktitle},{self.bookauthor}"
