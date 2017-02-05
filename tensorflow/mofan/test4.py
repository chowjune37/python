import tensorflow

input1 = tensorflow.placeholder(tensorflow.float32,[None,9.])
input2 = tensorflow.placeholder(tensorflow.float32,[None,8.])

output = tensorflow.matmul(input1,input2)

with tensorflow.Session() as sess:
    print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))
