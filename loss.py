import tensorflow as tf
###损失函数#######


def loss(logits,label_batches):
     cross_entropy=tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits,labels=label_batches)
     #主要实现两步Softmax以及交叉熵计算
     cost = tf.reduce_mean(cross_entropy)
     tf.summary.scalar("loss", cost)
     return cost