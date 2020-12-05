from . import fetch_data_api 
 

def song_url(name):
    client_id = 'e55a0893bd7f4c7e9628fe6ee58f4324'
    client_secret = 'a434335709d84dac9c222a941db65c30'
    sp = fetch_data_api.sp_api(client_id,client_secret)
    result = sp.search(q=name, limit=1)
    result = result['tracks']
    result = result['items']
    result = result[0]
    return (result['external_urls'])['spotify'],sp

#print(song_url('tum hi ho'))
