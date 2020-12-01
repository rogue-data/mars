from . import song_url
from . import get_features
from . import cs_model
import pandas as pd
import os

def recommend_songs(song,mode='default'):
    mody=mode
    path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'wd/dataset/final_dataset.csv')
    # Fetch url
    url = song_url.song_url(song)
    # Get the metadata
    track = get_features.getTrackFeatures(url)
    # Store the metadata into our dataframe
    df = pd.read_csv(path)
    df.loc[len(df)] = track
    # Sort by year
    df = df.sort_values(by='year')
    # Save the dataframe
    df.to_csv(path, index=False)
    # Find the similarity of the songs
    return cs_model.recommend_cosine(df,mody)


# print(recommend_songs('Tum Hi Ho Arjit Singh'))
