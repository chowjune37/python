import tensorflow
import numpy
import matplotlib.pyplot

def add_layer(inputs,in_size,out_size,activation_function=None):
    Weights = tensorflow.Variable(tensorflow.random_normal([in_size,out_size]))
    biases = tensorflow.Variable(tensorflow.zeros([1,out_size])+0.1)
    Wx_plus_b = tensorflow.matmul(inputs,Weights)+biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

x_data = numpy.linspace(-1,1,11)[:,numpy.newaxis]

y_data = numpy.square(x_data)

xs = tensorflow.placeholder(tensorflow.float32,[None,1])
ys = tensorflow.placeholder(tensorflow.float32,[None,1])

# l1 = add_layer(xs,1,6,activation_function=tensorflow.nn.relu)
# prediction = add_layer(l1,6,1,activation_function=None)

# one
Weights1 = tensorflow.Variable(tensorflow.random_normal([1,6]))
# biases1 = tensorflow.Variable(tensorflow.zeros([1,6])+0.1)
Wx_plus_b1 = tensorflow.matmul(xs,Weights1)
l1 = tensorflow.nn.relu(Wx_plus_b1)

# two
Weights2 = tensorflow.Variable(tensorflow.random_normal([6,1]))
# biases2 = tensorflow.Variable(tensorflow.zeros([1,1])+0.1)
prediction = tensorflow.matmul(l1,Weights2)


loss = tensorflow.reduce_mean(tensorflow.reduce_sum(tensorflow.square(ys - prediction),reduction_indices=[1]))
train_step = tensorflow.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tensorflow.global_variables_initializer()
sess = tensorflow.Session()
sess.run(init)

fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data,y_data)
matplotlib.pyplot.ion()
matplotlib.pyplot.show()

for i in range(1000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i % 100 == 0:
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
        print(sess.run(Weights1,feed_dict={xs:x_data,ys:y_data}))
        # print(sess.run(biases1,feed_dict={xs:x_data,ys:y_data}))
        print(sess.run(l1,feed_dict={xs:x_data,ys:y_data}))
        print(sess.run(Weights2,feed_dict={xs:x_data,ys:y_data}))
        # print(sess.run(biases2,feed_dict={xs:x_data,ys:y_data}))
        print(sess.run(prediction,feed_dict={xs:x_data,ys:y_data}))
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction,feed_dict={xs:x_data})
        lines = ax.plot(x_data,prediction_value,'r-',lw=5)
        matplotlib.pyplot.pause(0.2)

