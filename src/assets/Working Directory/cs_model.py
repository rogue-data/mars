from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def recommend_cosine(data):
    song_df = data.loc[len(data) - 1, :]
    song_df = pd.DataFrame(song_df).T
    song_df.drop(columns='key', inplace=True)
    similarity_data = data.copy()

    data_values = similarity_data.loc[:, ['acousticness', 'danceability',
                                          'energy', 'instrumentalness', 'liveness', 'loudness', 'mode',
                                          'speechiness', 'tempo', 'valence']]
    similarity_data['Similarity with song'] = cosine_similarity(data_values, data_values.to_numpy()[
        song_df.index[0], None]).squeeze()
    return (similarity_data.sort_values(by='Similarity with song', ascending=False)[1:6]).name
