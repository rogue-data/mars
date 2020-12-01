from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def recommend_cosine(data,mode):
    song_df = data.loc[len(data) - 1, :]
    song_df = pd.DataFrame(song_df).T
    song_df.drop(columns='key', inplace=True)
    similarity_data = data.copy()

    if mode=='default':
        data_values = similarity_data.loc[:, ['acousticness', 'danceability',
                                          'energy', 'instrumentalness', 'liveness', 'loudness', 'mode',
                                          'speechiness', 'tempo', 'valence']]
    elif mode=='peace':
        data_values = similarity_data.loc[:, ['acousticness','energy','loudness','speechiness', 'tempo', 'valence']]
    elif mode=='work':
        data_values = similarity_data.loc[:, ['instrumentalness', 'liveness','speechiness', 'tempo', 'valence']]
    elif mode=='party':
        data_values = similarity_data.loc[:, ['danceability','energy', 'instrumentalness', 'liveness', 'loudness','tempo', 'valence']]
    elif mode=='workout':
        data_values = similarity_data.loc[:, ['energy','loudness','mode','speechiness','tempo','valence']]
    
    similarity_data['Similarity with song'] = cosine_similarity(data_values, data_values.to_numpy()[
        song_df.index[0], None]).squeeze()
        
    # sending the complete data
    return (similarity_data.sort_values(by='Similarity with song', ascending=False)[1:6])
