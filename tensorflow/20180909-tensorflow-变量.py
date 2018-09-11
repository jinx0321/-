import tensorflow as tf

x=tf.Variable([1,2])
a=tf.Variable([3,3])

#增加一个减法op
sub=tf.subtract(x,a)

#增加一个加法op
add=tf.add(x,a)

#变量必须初始化
init =tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    reslut1=sess.run(sub)
    reslut2 =sess.run(add)
    print(reslut1)
    print(reslut2)


state=tf.Variable(0,name='counter')
add1=tf.add(state,1)
update=tf.assign(state,add1)
init =tf.global_variables_initializer()
with tf.Session() as sess:
   sess.run(init)
   for i in range(0,100):
        result=sess.run(update)
        print(result)


