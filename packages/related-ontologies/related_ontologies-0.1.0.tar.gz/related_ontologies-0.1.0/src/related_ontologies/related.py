import re
import time
import pandas as pd
import jaro
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from ftfy import fix_text

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def ngrams(string: str, n=10) -> list:
    """
    Takes an input string, cleans it and converts to ngrams.
    :param string: str
    :param n: int
    :return: list
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


def generateRelatedOntologies(query: str, choices: list, method: str) -> list:
    """
    Generates ontologies in choices that are related to the query based on the method selected.
    :param query: str
    :param choices: list
    :param method: str (partial_ratio, jaro_winkler, tf_idf)
    :return: list
    """
    if method == 'partial_ratio':
        query = list(query)
        related = process.extractBests(query, choices, scorer=fuzz.partial_ratio, limit=100)
    elif method == 'jaro_winkler':
        related = 1.0
    elif method == 'tf_idf':
        related = 2.0
    else:
        related = 0.0
    return related


def partial_ratio(string_1: str, string_2: str) -> float:
    """
    Calculates the fuzzywuzzy partial ratio between 2 strings.
    :param string_1: str
    :param string_2: str
    :return: float
    """
    ratio = fuzz.partial_ratio(string_1.lower(), string_2.lower())
    return ratio


def jaro_winkler(string_1: str, string_2: str) -> float:
    """
    Calculates the Jaro-Winkler score between 2 strings.
    :param string_1: str
    :param string_2: str
    :return: float
    """
    score = jaro.jaro_winkler_metric(string_1.lower(), string_2.lower())
    return score


def tf_idf(list_of_ontologies: list) -> float:
    """
    Calculates the cosine similarity between 2 strings after Term Frequency - Inverse Document Frequency Vectorization.
    :param list_of_ontologies: list
    :return: float
    """
    t1 = time.time()

    vectorizer = TfidfVectorizer(min_df=1, analyzer=ngrams)
    tf_idf_matrix = vectorizer.fit_transform(list_of_ontologies)

    t = time.time() - t1
    print("Time:", t)
    print(tf_idf_matrix.shape)

    score = 0.0
    return score
