import sys

from pyspark.sql import Row, Column

from social_senstiment.data import post_sentiments
from social_senstiment.utils.schema import SCHEMA as schema
from social_senstiment.spark.core.session import SPARK_SESSION as spark
from social_senstiment.spark.core.streaming import SPARK_STREAMING_CONTEXT as ssc
from social_senstiment.spark.ml.pipeline import PIPELINE as pipeline


# define the function to get the predicted sentiment on the received post
def get_prediction(post: str):
	try:
        #  remove the blank tweets and create the dataframe with each row contains a tweet text
		rowRdd = post.filter(lambda x: len(x) > 0).map(lambda w: Row(tweet=w))
		wordsDataFrame = spark.createDataFrame(rowRdd)
		# get the sentiments for each row
		model.transform(wordsDataFrame).select('tweet','prediction').show()
	except : 
		print('No stream is provided...')



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("[ERROR]. Please define host and port number", file=sys.stderr)
        sys.exit(-1)

    # reading the data set
    print('\n\nReading the dataset...........................\n')
    data = spark.read.csv(post_sentiments, schema=schema, header=True)

    print('\n\nFit the pipeline with the training data.......\n')
    model = pipeline.fit(data)  # for sklearn it is `estimator.fit(train_data)` [for testing]
    # estimator = model.stages[-1]
    # print(dir(estimator))             # get necessary information about estimator
    print('\n\nModel Trained....Waiting for the Data!!!!!!!!\n')
    HOST, PORT = sys.argv[1], int(sys.argv[2])
    lines = ssc.socketTextStream(HOST, PORT)
    post = lines.flatMap(lambda line : line.split('TWEET_APP'))  # change this to FACEBOOK_APP

    post.foreachRDD(get_prediction)

    ssc.start()             # Start the computation
    ssc.awaitTermination()  # Wait for the computation to terminate
