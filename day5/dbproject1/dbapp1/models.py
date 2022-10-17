from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Book(models.Model):
    booktitle = models.CharField(max_length=50)
    bookauthor = models.CharField(max_length=50)
    class Meta:
        db_table = "books"