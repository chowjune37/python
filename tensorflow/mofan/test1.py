import numpy
import tensorflow

x_data = numpy.random.rand(100).astype(numpy.float32)
y_data = x_data*0.1+0.3

Weight = tensorflow.Variable(tensorflow.random_uniform([1],-1.0,1.0))
biases = tensorflow.Variable(tensorflow.zeros([1]))

y = Weight*x_data+biases

loss = tensorflow.reduce_mean(tensorflow.abs(y-y_data))
optimizer = tensorflow.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tensorflow.global_variables_initializer()

sess = tensorflow.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step%20==0:
        print(step,sess.run(loss),sess.run(Weight),sess.run(biases))

