import tensorflow as tf


#线代
#创建一个常量op
m1 =tf.constant([[3,3]])
m2=tf.constant([[2],[3]])

#创建一个矩阵乘法,m1*m2
product=tf.matmul(m1,m2)


#定义一个绘画，启动默认图
with tf.Session() as sess:
    result = sess.run(product)
    print(result)

