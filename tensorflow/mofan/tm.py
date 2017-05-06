import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def layer(input,in_size,out_size,act=None):
	Weights = tf.Variable(tf.random_normal([in_size,out_size]))
	Biases = tf.Variable(tf.zeros([1,out_size])+0.1)
	ys = tf.matmul(input,Weights) + Biases
	if act == None:
		out = ys
	else:
		out = act(ys)
	return out


x = np.linspace(-1,1,1000).astype(np.float32)[:,np.newaxis]
noise = (np.random.rand(1000) / 10)[:,np.newaxis]
y = np.square(x) + noise + 0.5

xs = tf.placeholder(tf.float32,[None,1])
ys = tf.placeholder(tf.float32,[None,1])

l1 = layer(x,1,10,act = tf.nn.relu)
l2 = layer(l1,10,1,act = None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(y - l2),reduction_indices=[1]))
optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x,y)
plt.ion()
plt.show()

# 	sess.run(train)
# 	if i%100 == 0:
# 		print(sess.run(loss))
# 		print(sess.run(l2))
# print(y)
for i in range(1000):
    sess.run(train)
    if i % 50 == 0:
	    print(sess.run(loss))
	    try:
	        ax.lines.remove(lines[0])
	    except Exception:
	        pass
	    prediction_value = sess.run(l2)
	    lines = ax.plot(x,prediction_value,'r-',lw=5)
	    plt.pause(0.2)