import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def load_data(path):
    df = pd.read_csv(path)
    df = df.fillna('')
    df['content'] = df['description'] + ' ' + df['event'] + \
        ' ' + df['main_speaker'] + ' ' + df['name'] + \
        ' ' + df['speaker_occupation'] + \
        ' ' + df ['tags'] + ' ' + df['title']
    return df

def compute_cosine_similiarities(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['content'])
    cosine_similiarities = linear_kernel(X, X)
    return cosine_similiarities

def get_recommendations(title, df, cosine_similiarities):
    # Get the index of the TED Talk
    idx = df[df['title'] == title].index[0]
    # Get the pairwise similiarity scoresa
    sim_scores= list(enumerate(cosine_similiarities[idx]))
    # Sort the TED Talks based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the scores of the 10 most similar TED Talks
    sim_scores = sim_scores[1:11]
    # Get the TED Talks indices
    talk_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[talk_indices] # return the top 10 most similar TED Talks

if __name__ == "__main__":
    df = load_data('/home/ai/DEV_PROGRAMMING/Python/Pandas/AndroidStudio_PandasIntroduction/ted_main.csv')
    cosine_similiarities = compute_cosine_similiarities(df)
    print(get_recommendations('The power of vulnerability', df, cosine_similiarities))
