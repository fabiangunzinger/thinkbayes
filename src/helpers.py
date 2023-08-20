
from os.path import basename, exists, join

import pandas as pd

def download(url):
    filename = basename(url)
    filepath = join('data', filename)
    if not exists(filepath):
        from urllib.request import urlretrieve
        local, _ = urlretrieve(url, filepath)
        print('Downloaded ' + local)


def prob(A):
    """Computes the probability of a proposition, A."""    
    return A.mean()


def conditional(proposition, given):
    """Probability of A conditioned on given."""
    return prob(proposition[given])

