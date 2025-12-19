from django.urls import path
from .views  import *
urlpatterns = [
    path('get',UserView.as_view(),name='user_class')
]