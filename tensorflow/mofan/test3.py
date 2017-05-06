import tensorflow

state = tensorflow.Variable(0,name='counter')

#print(state.name)

one = tensorflow.constant(1)

new_value = tensorflow.add(state,one)
updata = tensorflow.assign(state,new_value)

init = tensorflow.global_variables_initializer()

with tensorflow.Session() as sess:
    sess.run(init)
    for _ in range(4): 
        sess.run(updata)
        print(sess.run(state))

