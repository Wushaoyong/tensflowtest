# import tensorflow as tf
# tf.compat.v1.disable_eager_execution()
# hello=tf.constant('hello,tensorflow')
# sess=tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True))
# print(sess.run(hello))
#
# #compat.v1. import tensorflow as tf+
# # sess=tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True))
#
#
#
# # -*- coding: utf-8 -*-
# """
# Spyder Editor
#
# 问题产生的原因：无法执行sess.run()的原因是tensorflow版本不同导致的，tensorflow版本2.0无法兼容版本1.0.
#
# 解决办法：tf.compat.v1.disable_eager_execution()
#
# 1 i                                                 mport tensorflow as tf2 tf.compat.v1.disable_eager_execution()
# 3 hello = tf.constant('Hello, TensorFlow!')
# 4 config = tf.compat.v1.ConfigProto(allow_soft_placement=True)
# 5 config.gpu_options.per_process_gpu_memory_fraction = 0.9
# 6 sess= tf.compat.v1.Session(config=config)
# 7 print(sess.run(hello))
# This is a temporary script file.
# """
#
#
import pydicom
path=pydicom.read_file(r'E:\data_canaer\LIDC-IDRI\LIDC-IDRI-0001\01-01-2000-30178\3000566.000000-03192\1-001.dcm')
print(path)