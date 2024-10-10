import os
import zipfile
import kaggle

from kaggle.api.kaggle_api_extended import KaggleApi

# Instantiate the API class
api = KaggleApi()

# Authenticate the API
api.authenticate()

# Define the path where you want to download the dataset
path = './' # current directory

# Download the dataset
api.dataset_download_file('rounakbanik/ted-talks', 'ted_main.csv', path=path, force=True)

# Unzip the dataset file
with zipfile.ZipFile(os.path.join(path, "ted_main.csv.zip"), 'r') as zip_ref:
    zip_ref.extractall(path)


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def process_ted_talks(filename):
    df = pd.read_csv(filename)
    df = df.fillna('')

    df['content'] = df['description'] + ' ' + df['event'] +\
        ' ' + df['main_speaker'] + ' ' + df['name'] + \
        ' ' + df['speaker_occupation'] + \
        ' ' + df['tags'] + ' ' + df['title']

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['content'])

    return X
