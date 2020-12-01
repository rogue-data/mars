from django.shortcuts import render
from .wd import recommend_songs
# Create your views here.

def home(request,song_name='alone',mode='default'):

    recommendations=recommend_songs.recommend_songs(song_name,mode)
    
    return render(request,'index.html')
