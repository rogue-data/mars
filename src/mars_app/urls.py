from django.urls import path
from . import views

urlpatterns = [
    path('song', views.song_func,name='song'),
    path('', views.welcome,name='home'),
]