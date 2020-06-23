from pyspark.streaming import StreamingContext

from .context import SPARK_CONTEXT as sc

SPARK_STREAMING_CONTEXT = StreamingContext(sc, batchDuration=3)
