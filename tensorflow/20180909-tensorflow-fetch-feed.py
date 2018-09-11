import tensorflow as tf

#Fetch
input1=tf.constant(5.0)
input2=tf.constant(5.0)

add=tf.add(input1,input2)
mul=tf.multiply(input1,add)

with tf.Session() as sess:
    reslut=sess.run([mul,add])
    print (reslut)

#Feed

#创建占位符
input3=tf.placeholder(tf.float32)
input4=tf.placeholder(tf.float32)

output=tf.multiply(input3,input4)

with tf.Session() as sess:
    #Feed的数据以字典的形式传入
    print(sess.run(output,feed_dict={input3:[7.0],input4:[3.0]}))
