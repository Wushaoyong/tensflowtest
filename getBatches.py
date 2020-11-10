import tensorflow as tf
######    get batches 　输入图片转换为tensor以及线程控制程序  ＃＃＃＃＃＃＃＃＃

def get_batches(image, label, resize_w, resize_h, batch_size, capacity):
    # convert the list of images and labels to tensor
    image = tf.cast(image, tf.string)
    label = tf.cast(label, tf.int64)
    queue = tf.train.slice_input_producer([image, label],shuffle=True,num_epochs=100)
    #将这个列表中的数据取出来放到文件队列里面，以便内存队列调用
    label = queue[1]
    image_c = tf.read_file(queue[0])
    image = tf.image.decode_jpeg(image_c, channels=3)
#将image_c图片采用3通道的方式进行读取
    #image = tf.image.resize_images(image, [resize_w, resize_h], method=2)
    image = tf.image.resize_image_with_crop_or_pad(image, resize_w, resize_h)   #把image的尺寸大小规范为resize_w*resize_h
    image = tf.image.per_image_standardization(image)
#将整幅图片标准化（不是归一化），加速神经网络的训练
    image_batch, label_batch = tf.train.batch([image, label], batch_size=batch_size,num_threads=1, capacity=capacity,allow_smaller_final_batch=False)
    #这里的train_batch主要是用于产生训练的batch
    images_batch = tf.cast(image_batch, tf.float32)
    labels_batch = tf.reshape(label_batch, [batch_size])
#将label_batch变换为参数[batch_size]形式
    return images_batch, labels_batch
