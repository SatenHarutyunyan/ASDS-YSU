import tensorflow as tf
from lin_reg import LinearRegressor


X = tf.random.uniform(shape=(1000, 1), minval=0, maxval=1, dtype=tf.float32)
y = tf.map_fn(lambda x: tf.sqrt(1 + x), X)


#  Model encapsulates all requirements from homework
iterative_model = LinearRegressor(lr_type="iterative")
analytic_model = LinearRegressor(lr_type="analytic")
lib_model = LinearRegressor(lr_type="sklearn")

# choose which model you want to be yours
model = iterative_model 

model.learn_from(X, y)
model.predict_for(X)
print(model.mse_loss)
print(model.parameters)
model.show()
