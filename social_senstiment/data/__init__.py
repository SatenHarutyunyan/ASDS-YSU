import os
import pyspark.sql.types as T


here = os.path.dirname(__file__)

tweet_sentiments = os.path.join(here, "tweet_sentiments.csv")
