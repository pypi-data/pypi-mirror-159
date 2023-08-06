import re
import time
import pandas as pd
from ftfy import fix_text

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def ngrams(string, n=10):
    """
    Takes an input string, cleans it and converts to ngrams.
    """
    string = str(string)
    string = string.lower()  # lower case
    string = fix_text(string)  # fix text
    string = string.encode("ascii", errors="ignore").decode()  # remove non ascii chars
    chars_to_remove = [")", "(", ".", "|", "[", "]", "{", "}", "'", "-"]
    rx = '[' + re.escape(''.join(chars_to_remove)) + ']'  # remove punc, brackets etc...
    string = re.sub(rx, '', string)
    string = string.replace('&', 'and')
    string = string.title()  # normalise case - capital at start of each word
    string = re.sub(' +', ' ', string).strip()  # get rid of multiple spaces and replace with a single
    string = ' ' + string + ' '  # pad names for ngrams...
    ngrams = zip(*[string[i:] for i in range(n)])
    return [''.join(ngram) for ngram in ngrams]


def generateRelatedOntologies(query: str) -> pd.DataFrame:
    return


def partial_ratio():
    return


def jaro_winkler():
    return


def tf_idf(list_of_ontology):
    t1 = time.time()

    vectorizer = TfidfVectorizer(min_df=1, analyzer=ngrams)
    tf_idf_matrix = vectorizer.fit_transform(list_of_ontology)

    t = time.time() - t1
    print("Time:", t)
    print(tf_idf_matrix.shape)
    return
