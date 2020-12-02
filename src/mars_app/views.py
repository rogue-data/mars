from django.shortcuts import render
from .wd import recommend_songs,download_songs
# Create your views here.

song='alone'
def song_func(request,mode='default'):
    song=request.GET['song_play']
    # Download song
    download_songs.download_song(song)
    # Get Recommendations
    crr,recommendations=recommend_songs.recommend_songs(song,mode)
    # print(crr.name)
    print(recommendations) 
    return render(request,'index.html',{'crr':crr,'rc':recommendations})

def home(request):
    return render(request,'index.html')
