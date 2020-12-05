from . import song_url
from . import get_features
from . import cs_model
import pandas as pd
import os
 
def recommend_songs(song,mode='default'):
    mody=mode
    print(f"Mode: {mody}")
    path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'wd/dataset/final_dataset.csv')
    # Fetch url
    print(song)
    url,sp = song_url.song_url(song)
    # Get the metadata
    track = get_features.getTrackFeatures(url,sp)
    # Store the metadata into our dataframe
    print('st start')
    df = pd.read_csv(path)
    df.loc[len(df)] = track[0]
    current_song={'name':track[2],'artist':track[3],'img':track[1],'year':track[4],'album':track[5]}
    # current_song=pd.DataFrame(current_song)
    # Sort by year
    df = df.sort_values(by='year')
    # df=df.sample(frac=1)
    # Save the dataframe
    df.drop_duplicates(subset='name',inplace=True)
    df.to_csv(path, index=False)
    print('st end')
    # Find the similarity of the songs
    #return cs_model.recommend_cosine(df,mody) , track[1]
    recommended_song_ids=cs_model.recommend_cosine(df,mody)
    #print(recommended_song_ids)
    recommended=pd.DataFrame(columns=['name','img','artist','year','album'])
    recommended=recommended.append(current_song,ignore_index=True)
    # for id in recommended_song_ids:
    #     # print(f"id: {id}")
    #     tracke=get_features.getTrackFeatures(id,sp)
    #     recommended=recommended.append({'name':tracke[2],'artist':tracke[3],'img':tracke[1],'year':tracke[4]},ignore_index=True)
    
    tracke=get_features.getTracksFeatures(recommended_song_ids,sp)
    for i in range(0,25):
        recommended=recommended.append({'name':tracke['tracks'][i]['name'],'artist':tracke['tracks'][i]['album']['artists'][0]['name'],'img':(tracke['tracks'][i]['album']['images'][0])['url'],'year':int(tracke['tracks'][i]['album']['release_date'][:4]),'album':tracke['tracks'][i]['album']['name']},ignore_index=True)
    return current_song , recommended


# print(recommend_songs('Tum Hi Ho Arjit Singh'))
