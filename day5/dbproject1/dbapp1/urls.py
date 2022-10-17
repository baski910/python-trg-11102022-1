from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('create',views.create,name='create'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('update/<int:id>',views.update,name='update')
]