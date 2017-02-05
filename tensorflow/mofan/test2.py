import tensorflow

matrix1 = tensorflow.constant([[3,3]])
matrix2 = tensorflow.constant([[2],[2]])

product = tensorflow.matmul(matrix1,matrix2)

sess = tensorflow.Session()
result = sess.run(product)

print(result)

sess.close()
