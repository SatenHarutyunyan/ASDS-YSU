import pyspark.sql.types as T



SCHEMA = T.StructType([
				T.StructField(name='id', dataType=T.IntegerType(), nullable=True),
    			T.StructField(name='label', dataType=T.IntegerType(), nullable=True),
    			T.StructField(name='tweet', dataType=T.StringType(), nullable= True)    
    		])

