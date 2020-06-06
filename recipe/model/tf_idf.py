import pandas as pd
import numpy as np
from scipy import sparse

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans


def tf_idf_from_matrix(M):
    M = M.toPandas().values
    counts_M = sparse.csr_matrix(M)
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(counts_M)
    return tfidf.toarray()

def kmeans_clusters(num_of_cl, data):
    kmeans = KMeans(init='k-means++', 
    n_clusters=num_of_cl, n_init=10)
    kmeans.fit(data)
    return kmeans.predict(data)
