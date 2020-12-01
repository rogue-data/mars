import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def sp_api(client_id, client_secret):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                               client_secret=client_secret))
    return sp