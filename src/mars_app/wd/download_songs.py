from youtube_search import YoutubeSearch
from subprocess import Popen,PIPE
import subprocess,sys
# import os
  
def download_song(name,album):
    print('d start')
    result = YoutubeSearch(name+''+album, max_results=1).to_dict()
    url='https://www.youtube.com/watch?v='+result[0]['id']
    x=str(subprocess.check_output(["youtube-dl","-g","-x", url])).split("\\n")[0].split('b\'')[1]
    print('d end')
    return x