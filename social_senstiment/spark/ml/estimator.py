from pyspark.ml.classification import LogisticRegression

# tested and loaded best hyperparameters
ESTIMATOR = LogisticRegression(featuresCol='vector', labelCol='label', predictionCol="prediction",
                 maxIter=1000, regParam=0.0, elasticNetParam=0.0, tol=1e-6, fitIntercept=True,
                 threshold=0.5, thresholds=None, probabilityCol="probability",
                 rawPredictionCol="rawPrediction", standardization=True, weightCol=None,
                 aggregationDepth=3, family="auto",
                 lowerBoundsOnCoefficients=None, upperBoundsOnCoefficients=None,
                 lowerBoundsOnIntercepts=None, upperBoundsOnIntercepts=None)
