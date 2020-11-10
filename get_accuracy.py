import tensorflow as tf
#######获得精确数据#########

def get_accuracy(logits,labels):
    acc = tf.nn.in_top_k(logits,labels,1)
    #tf.nn.in_top_k组要是用于计算预测的结果和实际结果的是否相等，返回一个bool类型的张量
    acc = tf.cast(acc,tf.float32)
    acc = tf.reduce_mean(acc)
    return acc