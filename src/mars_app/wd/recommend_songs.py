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
    url = song_url.song_url(song)[0]
    sp= song_url.song_url(song)[1]
    # Get the metadata
    track = get_features.getTrackFeatures(url,sp)
    # Store the metadata into our dataframe
    df = pd.read_csv(path)
    df.loc[len(df)] = track[0]
    current_song={'name':track[2],'artist':track[3],'img':track[1],'year':track[4]}
    # current_song=pd.DataFrame(current_song)
    # Sort by year
    df = df.sort_values(by='year')
    # Save the dataframe
    df.drop_duplicates(subset='name',inplace=True)
    df.to_csv(path, index=False)
    # Find the similarity of the songs
    #return cs_model.recommend_cosine(df,mody) , track[1]
    recommended_song_ids=cs_model.recommend_cosine(df,mody)
    #print(recommended_song_ids)
    recommended=pd.DataFrame(columns=['name','img','artist','year'])
    for id in recommended_song_ids:
        # print(f"id: {id}")
        tracke=get_features.getTrackFeatures(id,sp)
        recommended=recommended.append({'name':tracke[2],'artist':tracke[3],'img':tracke[1],'year':tracke[4]},ignore_index=True)
    return current_song , recommended


# print(recommend_songs('Tum Hi Ho Arjit Singh'))
