from django.shortcuts import render
from .wd import recommend_songs,download_songs
from json import dumps 
# Create your views here.

song='alone'
def song_func(request,mode='default'):
    song=request.GET['song_play']
    mode=int(request.GET['mode'])
    modes_list=['','default','peace','work','party','workout']
    print(f"Mode in Views.py:: {mode}")
    # Get Recommendations
    print(modes_list[mode])
    print(song)
    crr,recommendations=recommend_songs.recommend_songs(song,modes_list[mode])
    # Download song
    download_songs.download_song(song,crr['artist'])
    # print(crr.name)
    # print(recommendations)
    # dataJSON = dumps(recommendations) 
    dataJSON=recommendations.to_json()
    dataJSON=dumps(dataJSON)
    # print(dataJSON)
    return render(request,'index.html',{'crr':crr,'rc':recommendations,'mode':(mode-1)*5,'dt':dataJSON})

def welcome(request):
    return render(request,'welcome.html')
