from youtube_search import YoutubeSearch
import pafy
import os
 
def download_song(name,artist):
    path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'static/songs/')
    os.chdir(path)
    try:
        os.remove('0.mp3')
    except:
        print("nothing")
    result = YoutubeSearch(name+''+artist, max_results=1).to_dict()
    url='https://www.youtube.com/watch?v='+result[0]['id']
    video = pafy.new(url) 
    audiostreams = video.audiostreams 
    
    audiostreams[0].download()
    #renaming
    #print(f"Location: {os.listdir()}")
    os.rename((os.listdir())[0],"0.mp3")
# download_song('Darkside')