import tensorflow as tf
import numpy as np

x = tf.Variable(tf.random_normal([4,5]))

y = tf.nn.softmax(x)

init = tf.global_variables_initializer()
sess = tf.Session()

sess.run(init)

print(sess.run(x))
print(sess.run(x))