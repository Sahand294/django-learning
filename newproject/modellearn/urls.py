from django.urls import path

from .views import createPerson

urlpatterns = [
    path('create', createPerson),
]