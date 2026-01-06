from django.urls import path

from .views import *

urlpatterns = [
    path('create', createPerson),
    path('register', show_register),
    path('read', read_person,name='read'),
    path('delete/<int:id>', delete_person,name='delete'),
    path('update/<int:id>', update_person,name='update')
]