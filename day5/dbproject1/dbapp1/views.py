from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Book
from .forms import BookForm

# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request,'dbapp1/home.html',{'books':books})

def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('dbapp1:home'))
    else:
        form = BookForm()
        return render(request, 'dbapp1/home.html',{'form': form})

def edit(request, id):
    book = Book.objects.get(id=id)
    #form = BookForm(book)
    return render(request, 'dbapp1/edit.html', {'book': book})

def update(request,id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST, instance = book)
    if form.is_valid():
        form.save()
        return redirect(reverse('dbapp1:home'))
    form = BookForm(book)
    return render(request,'dbapp1/edit.html',{'book': book})





