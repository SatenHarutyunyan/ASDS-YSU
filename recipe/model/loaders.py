from types import FunctionType

from pyspark.sql import functions as F
from pyspark.sql import types as T
from pyspark.sql import Row

from recipe.spark import spark


class SparkDataLoader:

    def __init__(self, path: str, label_col: str, drop_cols: list, transformer: FunctionType):
        self.path = path
        self.label_col = label_col
        self.drop_cols = drop_cols
        self.transformer = transformer
        
        self.process()

    def process(self):
        self._transform(
            self._drop_c(
                self._read(

                )
            )
        )


    def labels(self, is_distinct: bool):
        if is_distinct:
            return self._data.select(self.label_col).distinct().rdd.flatMap(lambda x : x).collect()
        return self._data.select(self.label_col).rdd.flatMap(lambda x : x).collect()
    
    def _read(self):
        self._data = spark.read.json(self.path, multiLine=True)
        return self._data

    def _drop_c(self, data):
        return data.select([c for c in data.columns if c not in self.drop_cols])

    def _transform(self, data):
        t_data = self.transformer(data)
        self.data = spark.createDataFrame(Row(**t_data[x]) for x in t_data)

    def describe(self):
        self.data.describe()
    
    def show(self, count: int=5):
        self.data.show(count)

    

