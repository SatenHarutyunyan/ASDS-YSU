# from pyspark.ml.feature import StringIndexer, OneHotEncoderEstimator, VectorAssembler
import sys

from pyspark.sql import Row, Column

from social_senstiment.data import tweet_sentiments
from social_senstiment.utils.schema import SCHEMA as schema
from social_senstiment.spark.core.session import SPARK_SESSION as spark
from social_senstiment.spark.core.streaming import SPARK_STREAMING_CONTEXT as ssc
from social_senstiment.spark.ml.pipeline import PIPELINE as pipeline


# define the function to get the predicted sentiment on the data received
def get_prediction(tweet_text: str) -> None:
	try:
        #  remove the blank tweets and create the dataframe with each row contains a tweet text
		rowRdd = tweet_text.filter(lambda x: len(x) > 0).map(lambda w: Row(tweet=w))
		wordsDataFrame = spark.createDataFrame(rowRdd)
		# get the sentiments for each row
		estimator.transform(wordsDataFrame).select('tweet','prediction').show()
	except : 
		print('No stream is provided...')



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("[ERROR]. Please define host and port number", file=sys.stderr)
        sys.exit(-1)

    # reading the data set
    print('\n\nReading the dataset...........................\n')
    my_data = spark.read.csv(tweet_sentiments, schema=schema, header=True)

    print('\n\nFit the pipeline with the training data.......\n')
    estimator = pipeline.fit(my_data)

    print('\n\nModel Trained....Waiting for the Data!!!!!!!!\n')
    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    post = lines.flatMap(lambda line : line.split('TWEET_APP'))  # change this to FACEBOOK_APP

    post.foreachRDD(get_prediction)

    ssc.start()             # Start the computation
    ssc.awaitTermination()  # Wait for the computation to terminate
