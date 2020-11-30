from youtube_search import YoutubeSearch
import pafy
import os
 
def download_song(name):
    os.chdir('./songs')
    try:
        os.remove('0.mp3')
    except:
        print("nothing")
    result = YoutubeSearch(name, max_results=1).to_dict()
    url='https://www.youtube.com/watch?v='+result[0]['id']
    video = pafy.new(url) 
    audiostreams = video.audiostreams
    #chosing song by quality 
    audiostreams[3].download(filepath="./songs")
    #renaming 
    #print(f"Location: {os.listdir()}")
    os.rename((os.listdir())[0],"0.mp3")
#download_song('tum hi ho')