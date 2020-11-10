import tensorflow as tf
###全连接层######

with tf.variable_scope('fc1') as scope:
    reshape = tf.reshape(pool8, shape=[batch_size, -1])
    dim = reshape.get_shape()[1].value
    print("参数个数:%r", dim)
    weights = tf.get_variable('weights', shape=[dim, 4096], dtype=tf.float32,
    initializer=tf.truncated_normal_initializer(stddev=0.005, dtype=tf.float32))
    biases = tf.get_variable('biases', shape=[4096], dtype=tf.float32,
    initializer=tf.constant_initializer(0.1))
    pre_activation = tf.add(tf.matmul(reshape, weights), biases)
    pre_activation = batch_norm(pre_activation, is_training_mmodel)
    fc1 = tf.nn.relu(pre_activation, name=scope.name)
    fc1 = tf.nn.dropout(fc1, dropout_num)
with tf.variable_scope('fc2') as scope:
    weights = tf.get_variable('fc2', shape=[4096, 2048], dtype=tf.float32,
    initializer=tf.truncated_normal_initializer(stddev=0.005, dtype=tf.float32))
    biases = tf.get_variable('biases', shape=[2048], dtype=tf.float32,
    initializer=tf.constant_initializer(0.1))
    pre_activation = tf.add(tf.matmul(fc1, weights), biases)
    pre_activation = batch_norm(pre_activation, is_training_mmodel)
    fc2 = tf.nn.relu(pre_activation, name=scope.name)
    fc2 = tf.nn.dropout(fc2, dropout_num)
with tf.variable_scope('softmax_linear') as scope:
   weights = tf.get_variable('softmax_linear', shape=[2048, 2], dtype=tf.float32,                     initializer=tf.truncated_normal_initializer(stddev=0.005, dtype=tf.float32))
   biases = tf.get_variable('biases', shape=[2], dtype=tf.float32,
   initializer=tf.constant_initializer(0.1))
   softmax_linear = tf.add(tf.matmul(fc2, weights), biases, name=scope.name)
   return softmax_linear