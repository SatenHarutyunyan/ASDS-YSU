from itertools import chain
from collections import Counter

from sklearn.decomposition import PCA

from recipe.data import train, test
from recipe.model.loaders import SparkDataLoader
from recipe.model.tf_idf import tf_idf_from_matrix, kmeans_clusters
from recipe.utils.funcs import map_labels_to_classes


def transform(data):
    unique_cuisines = data.select("cuisine").distinct().rdd.flatMap(lambda x : x).collect()
    data_ = {}
    for cuisine in unique_cuisines:
        data_[cuisine] = []
        ingredients = data.filter(data["cuisine"] == cuisine).select("ingredients")\
                    .rdd.flatMap(lambda x: x).collect()
        data_[cuisine] = Counter(list(chain.from_iterable(ingredients)))
    unique_ingredients = set()
    for cuisine in data_.keys():
        unique_ingredients.update(set(data_[cuisine]))
    data_df = {}
    def get_count(cuisine, ingredient, data_):
        return data_[cuisine][ingredient] if ingredient in data_[cuisine] else 0
    for cuisine in unique_cuisines:
        data_df[cuisine] = {
            ingredient: get_count(cuisine, ingredient, data_) for ingredient in unique_ingredients
            }
    return data_df


train_data = SparkDataLoader(
    path=train,
    label_col = "cuisine",
    drop_cols=["id"],
    transformer=transform
)

N_COMPONENTS = 2
N_CLUSTERS = 3

pca = PCA(n_components=N_COMPONENTS)

tf_idf_matrix = tf_idf_from_matrix(train_data.data)
r_data = pca.fit_transform(tf_idf_matrix)

class_labels = kmeans_clusters(N_CLUSTERS, r_data)
class_names = train_data.labels(is_distinct=True)


out = map_labels_to_classes(labels=class_labels, classes=class_names)

for group, countries in out.items():
    print(f"Group {group}: {list(countries)}" )

# test_data = SparkDataLoader(
#     path=test,
#     drop_cols=["id"],
#     transformer=transform
# )
