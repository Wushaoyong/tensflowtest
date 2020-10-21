import tensorflow as tf
a=tf.contant(10)
b=tf.contant(32)
sess=tf.Session()
print(sess.run(a+b))