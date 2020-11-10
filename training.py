import tensorflow as tf
######train函数#######


def training(loss,lr):
    train_op = tf.train.RMSPropOptimizer(lr,0.9).minimize(loss)
    #自适应学习率优化算法
    return train_op