from song_url import song_url
from get_features import getTrackFeatures
from cs_model import recommend_cosine
import pandas as pd


def recommend_songs(song):
    # Fetch url
    url = song_url(song)
    # Get the metadata
    track = getTrackFeatures(url)
    # Store the metadata into our dataframe
    df = pd.read_csv("./dataset/final_dataset.csv")
    df.loc[len(df)] = track
    # Sort by year
    df = df.sort_values(by='year')
    # Save the dataframe
    df.to_csv("./dataset/final_dataset.csv", index=False)
    # Find the similarity of the songs
    return recommend_cosine(df)


# print(recommend_songs('Tum Hi Ho Arjit Singh'))
