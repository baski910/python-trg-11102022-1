from django.urls import path
from .views import BookViews

urlpatterns = [
    path('books/',BookViews.as_view(),name="books"),
    path('books/<int:id>',BookViews.as_view(),name="book")
]