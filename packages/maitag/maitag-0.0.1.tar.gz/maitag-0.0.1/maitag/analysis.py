import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from spacy_language_model import nlp


def spacy_tokenizer(text, spacy_language_model=nlp):
    """ Return a list of str tokens using the spacy medium language model tokenizer"""
    return [t.text for t in spacy_language_model(text)]


def find_keywords(texts, tokenizer=spacy_tokenizer, min_df=1, max_df=1.0, stop_words=[], **kwargs):
    """ Find the most important word in each text from the max Compute the TF-IDF value """
    vectorizer = TfidfVectorizer(tokenizer=tokenizer, min_df=min_df, max_df=max_df, stop_words=stop_words, **kwargs)
    vectorizer.fit(texts)
    sparsevecs = vectorizer.transform(texts)
    word_indices = [row.argmax() for row in sparsevecs]
    vocab = np.array(vectorizer.get_feature_names_out())
    return list(vocab[word_indices])


def tfidf_df(texts, tokenizer=spacy_tokenizer, min_df=1, max_df=1.0, stop_words=[], **kwargs):
    """ Create a sparse DataFrame TF-IDF vectors (rows) from an array of strings """
    vectorizer = TfidfVectorizer(tokenizer=tokenizer, min_df=min_df, max_df=max_df, stop_words=stop_words, **kwargs)
    vectorizer.fit(texts)
    sparsevecs = vectorizer.transform(texts)
    sparsevecs = pd.DataFrame.sparse.from_spmatrix(sparsevecs)
    sparsevecs.columns = list(vectorizer.get_feature_names_out())
    return sparsevecs
