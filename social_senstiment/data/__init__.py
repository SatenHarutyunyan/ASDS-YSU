import os
import pyspark.sql.types as T


here = os.path.dirname(__file__)

post_sentiments = os.path.join(here, "post_sentiments.csv")
