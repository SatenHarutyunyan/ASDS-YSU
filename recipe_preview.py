from itertools import chain
from collections import Counter

from pyspark.sql import functions as F
from pyspark.sql import types as T
from pyspark.sql import Row

from recipe.spark import spark
from recipe.data import train, test



train_df = spark.read.json(train, multiLine=True)
train_df = train_df.drop("id")

# to see the shape of data
train_df.describe()
# .show



# to see wheter the data is balanced.
train_df\
    .groupBy("cuisine")\
        .count()\
            .orderBy("count", ascending=False).show()


# to see min, max, avg recepie size
len_udf = F.udf(lambda x: len(x), T.IntegerType())
train_df_with_len = train_df.withColumn('length', len_udf(train_df["ingredients"]))
train_df_with_len\
    .groupBy("cuisine")\
        .agg(
            F.max(train_df_with_len["length"]),
            F.min(train_df_with_len["length"]),
            F.avg(train_df_with_len["length"])
        )\
    .orderBy("avg(length)", ascending=False).show()


# get all unique cuisines
unique_cuisines = train_df.select("cuisine").distinct().rdd.flatMap(lambda x : x).collect()


# create dict of cusisines and ingedients
# data = {}
# for cuisine in unique_cuisines:
#     data[cuisine] = []
#     ingredients = train_df.filter(train_df["cuisine"] == cuisine).select("ingredients")\
#                 .rdd.flatMap(lambda x: x).collect()
#     data[cuisine] = Counter(list(chain.from_iterable(ingredients)))

# # get all unique ingredients
# unique_ingredients = set()
# for cuisine in data.keys():
#     unique_ingredients.update(set(data[cuisine]))


# def get_count(cuisine, ingredient, data):
#     return data[cuisine][ingredient] if ingredient in data[cuisine] else 0


# data_df = {}
# for cuisine in unique_cuisines:
#     data_df[cuisine] = {ingredient: get_count(cuisine, ingredient, data) for ingredient in unique_ingredients}

# final_df = spark.createDataFrame(Row(**data_df[x]) for x in data_df)

