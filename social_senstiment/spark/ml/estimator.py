from pyspark.ml.classification import LogisticRegression


ESTIMATOR = LogisticRegression(featuresCol='vector', labelCol='label') 
