from pyspark.sql.session import SparkSession

from .context import SPARK_CONTEXT

SPARK_SESSION = SparkSession(SPARK_CONTEXT)
