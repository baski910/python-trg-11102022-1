from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    books = models.Book.objects.all()
    return render(request,'dbapp1/home.html',{'books':books})
