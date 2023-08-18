
from os.path import basename, exists, join

import pandas as pd

def download(url):
    filename = basename(url)
    filepath = join('data', filename)
    if not exists(filepath):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(url, filepath)
        print('Downloaded ' + local)


def read_gss():
    """Add required columns to GSS DataFrame."""
    df = pd.read_csv('data/gss_bayes.csv', index_col=0)
    df['banker'] = df['indus10'] == 6870
    df['liberal'] = df['polviews'] <= 3
    df['democrat'] = df['partyid'] <= 1
    return df



