from . import fetch_data_api


def getTrackFeatures(id):
    client_id = 'e55a0893bd7f4c7e9628fe6ee58f4324'
    client_secret = 'a434335709d84dac9c222a941db65c30'
    sp = fetch_data_api.sp_api(client_id, client_secret)
    meta = sp.track(id)
    features = sp.audio_features(id)

    # meta
    name = meta['name']
    # album = meta['album']['name']
    artists = meta['album']['artists'][0]['name']
    # release_date = meta['album']['release_date']
    duration_ms = meta['duration_ms']
    popularity = meta['popularity']
    year = int(meta['album']['release_date'][:4])
    image_url=(meta['album']['images'][0])['url']

    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    mode = features[0]['mode']
    key = features[0]['key']
    valence = features[0]['valence']
    # time_signature = features[0]['time_signature']

    track = [acousticness, "['" + artists + "']", danceability, duration_ms, energy,
             id[-22:], instrumentalness, key, liveness, loudness,
             mode, name, popularity, speechiness, tempo,
             valence, year]
    return track, image_url , name , artists ,year