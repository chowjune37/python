import tensorflow

input1 = tensorflow.placeholder(tensorflow.float32,[None,None])
input2 = tensorflow.placeholder(tensorflow.float32,[None,1])

output = tensorflow.matmul(input1,input2)

with tensorflow.Session() as sess:
    print(sess.run(input1,feed_dict={input1:[[7,7],[8,8]]}))
