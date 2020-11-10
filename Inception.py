import tensorflow as tf
with tf.variable_scope('conv7') as scope:
    input_image = pool6
    input_1 = 110
    input_2 = 120
    input_3 = input_2 * 3
    weights = tf.get_variable('weights',shape=[3, 3, input_1, input_2],
dtype=tf.float32,
initializer=tf.truncated_normal_initializer(stddev=0.05, dtype=tf.float32))
    biases = tf.get_variable('biases',shape=[input_2],dtype=tf.float32,
    initializer=tf.constant_initializer(0.1))
weights_deduce = tf.get_variable('weights_deduce',shape=[3, 3, input_3, input_2],dtype=tf.float32, initializer=tf.truncated_normal_initializer
(stddev=0.05, dtype=tf.float32))
    biases_deduce = tf.get_variable('biases_deduce',shape=[input_2],
dtype=tf.float32,initializer=tf.constant_initializer(0.1))
    conv = tf.nn.conv2d(input_image, weights, strides=[1, 1, 1, 1], padding='SAME')
    pre_activation = tf.nn.bias_add(conv, biases)
    pre_activation = batch_norm(pre_activation, is_training_mmodel)
    conv_relu = tf.nn.relu(pre_activation, name=scope.name)
    pool_2_2 = tf.nn.max_pool(conv_relu, ksize=[1, 2, 2, 1], strides=[1, 1, 1, 1], padding='SAME', name='pooling2_2')
    pool_3_3 = tf.nn.max_pool(conv_relu, ksize=[1, 3, 3, 1], strides=[1, 1, 1, 1], padding='SAME', name='pooling3_3')
    pool_4_4 = tf.nn.max_pool(conv_relu, ksize=[1, 4, 4, 1], strides=[1, 1, 1, 1], padding='SAME', name='pooling4_4')
    pool_pre = tf.concat([pool_2_2, pool_3_3, pool_4_4], 3)
    with tf.variable_scope('reduce_layer') as deduce0:
        conv = tf.nn.conv2d(pool_pre, weights_deduce, strides=[1, 1, 1, 1], padding='SAME')
        pre_activation = tf.nn.bias_add(conv, biases_deduce)
        pre_activation = batch_norm2(pre_activation, is_training_mmodel)
        pool7 = tf.nn.relu(pre_activation, name=deduce0.name)