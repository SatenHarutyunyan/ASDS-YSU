from pyspark.ml import Pipeline

from .transformer import TRANSFORMERS
from .estimator import ESTIMATOR

PIPELINE = Pipeline(stages=[*TRANSFORMERS, ESTIMATOR])
