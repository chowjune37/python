import tensorflow
import numpy
import matplotlib.pyplot

def add_layer(inputs,in_size,out_size,n_layer,activation_function=None):
    layer_name = 'layer%s'%n_layer
    with tensorflow.name_scope(layer_name):
        with tensorflow.name_scope('weights'):
            Weights = tensorflow.Variable(tensorflow.random_normal([in_size,out_size]),name='W')
            tensorflow.histogram_summary(layer_name+'/weights',Weights)
        with tensorflow.name_scope('biases'):
            biases = tensorflow.Variable(tensorflow.zeros([1,out_size])+0.1,name='b')
            tensorflow.histogram_summary(layer_name+'/biases',biases)
        with tensorflow.name_scope('Wx_plus_b'):
            Wx_plus_b = tensorflow.matmul(inputs,Weights)+biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tensorflow.histogram_summary(layer_name+'/outputs',outputs)
        return outputs

x_data = numpy.linspace(-1,1,300)[:,numpy.newaxis]
noise = numpy.random.normal(0,0.05,x_data.shape)
y_data = numpy.square(x_data) - 0.5 + noise

# define placeholder for inputs to network
with tensorflow.name_scope('inputs'):
    xs = tensorflow.placeholder(tensorflow.float32,[None,1],name='x_input')
    ys = tensorflow.placeholder(tensorflow.float32,[None,1],name='y_input')

# add hidden layer
l1 = add_layer(xs,1,10,n_layer=1,activation_function=tensorflow.nn.relu)
# add hidden layer
prediction = add_layer(l1,10,1,n_layer=2,activation_function=None)

# the error between predicition and real data
with tensorflow.name_scope('loss'):
    loss = tensorflow.reduce_mean(tensorflow.reduce_sum(tensorflow.square(ys-prediction),reduction_indices=[1]))
    tensorflow.scalar_summary('loss',loss)
with tensorflow.name_scope('train'):
    train_step = tensorflow.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tensorflow.global_variables_initializer()
sess = tensorflow.Session()
merged = tensorflow.merge_all_summaries()
writer = tensorflow.train.SummaryWriter('logs/',sess.graph)

# important step
sess.run(init)

fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data,y_data)
matplotlib.pyplot.ion()
matplotlib.pyplot.show()

for i in range(1000):
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i % 50 == 0:
        result = sess.run(merged,feed_dict={xs:x_data,ys:y_data})
        writer.add_summary(result,i)
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction,feed_dict={xs:x_data})
        lines = ax.plot(x_data,prediction_value,'r-',lw=5)
        matplotlib.pyplot.pause(0.2)


