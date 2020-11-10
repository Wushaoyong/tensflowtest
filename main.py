import shutil

import tensorflow as tf
import inputData
import model
import numpy as np
import os

def run_training():
    #result=0
    #print("****最大值清0********")
    global data_dir,model_save_dir,log_tensorboard,test_dir,batch_size_set,input_img_size,capacity,information_save_root,AR,TPR,TNR,MAX_AR
    AR=0
    MAX_AR=0
    TPR=0
    TNR=0
    train = tf.Graph()
    with train.as_default():
        image, label = inputData.get_files(data_dir)
        image_batches, label_batches = inputData.get_batches(image, label, input_img_size, input_img_size, batch_size_set, capacity)
        keep_prob_train = tf.placeholder(tf.float32)
        p = model.mmodel(image_batches, batch_size_set,keep_prob_train,
    True)
        cost = model.loss(p, label_batches)
        train_op = model.training(cost, 0.001)
        acc = model.get_accuracy(p, label_batches)
        summary_op = tf.summary.merge_all()
        with tf.Session(graph=train) as sess:
            sess.run(tf.global_variables_initializer())
            sess.run(tf.local_variables_initializer())
# 这行是为了和tf.train.slice_input_producer中的设置对应起来
#因为tf.train.slice_input_producer中设置只读取13次数据，因此需要初始化局部变量num_epochs
            saver = tf.train.Saver(max_to_keep=1)
            coord = tf.train.Coordinator()
            threads = tf.train.start_queue_runners(sess=sess, coord=coord)
            train_writer = tf.summary.FileWriter(log_tensorboard, sess.graph)
            try:
                for step in np.arange(1000000):
                    print(step)
                    if coord.should_stop():
                        break
                    _, train_acc, train_loss,summary = sess.run([train_op, acc, cost,summary_op],feed_dict={keep_prob_train:0.5})
          print("loss:{} accuracy:{}".format(train_loss, train_acc))
        train_writer.add_summary(summary, step)
        if(step>3000 and step%500==0):
            check = os.path.join(model_save_dir, "model.ckpt")
            saver.Ssave(sess, check, global_step=step)
            np.test(test_dir)
            if(TP + FP + TN + FN !=0):
               AR = (TP + TN) / (TP + FP + TN + FN)  # 准确率
               if (TP + FN != 0):
                  TPR = TP / (TP + FN)  # 敏感性
                  if (TN + FP != 0):
                     TNR = TN / (TN + FP)  # 特异性
                     print("****test---result  ****")
                        print("TP:", TP)
                        print("FP:", FP)
                        print("TN:", TN)
                        print("FN:", FN)
                        print("AR:", AR)
                        print("TPR:", TPR)
                        print("TNR:", TNR)
                        print("*****test---result     ***")
        with open(information_save_root, 'a') as file:file.write("*******\n")
        file.write("训练集迭代步数："+str(step)+"    训练集的准确率："+str(train_acc)+"    训练集的损失值："+str(train_loss)+"\n")
        file.write("TP:" + str(TP) + "    FP:" + str(FP) + "    TN:" + str(TN) + "    FN:" + str(FN) +"\n")
        file.write("AR:" + str(AR) + "    TPR:" + str(TPR) + "    TNR:" + str(TNR) + "\n")
        with open(information_save_root_AR, 'a') as file2:
             file2.write(str(AR)+"  ")
             with open(information_save_root_TPR, 'a') as file3:
                 file3.write(str(TPR)+"  ")
             with open(information_save_root_TNR, 'a') as file4:
                 file4.write(str(TNR)+"  ")
             with open(information_save_root_TRAIN_ACC, 'a') as file5:
                 file5.write(str(train_acc)+"  ")
                 if(AR>MAX_AR):
                    MAX_AR = AR
                    path_model_save_1="G:/lung_cancer/32_32/model_save/model.ckpt-"+str(step)+".data-00000-of-00001"
                    path_model_save_2="G:/lung_cancer/32_32/note/best_model/model.ckpt-"+str(step)+".data-00000-of-00001"
                    path_model_save_3="G:/lung_cancer/32_32/model_save/model.ckpt-"+str(step)+".index"
                    path_model_save_4="G:/lung_cancer/32_32/note/best_model/model.ckpt-"+str(step)+".index"
                    path_model_save_5="G:/lung_cancer/32_32/model_save/model.ckpt-"+str(step)+".meta"
                    path_model_save_6="G:/lung_cancer/32_32/note/best_model/model.ckpt-"+str(step)+".meta"
                    path_model_save_7="G:/lung_cancer/32_32/model_save/checkpoint"
                    path_model_save_8="G:/lung_cancer/32_32/note/best_model/checkpoint"
                 if (os.path.exists(path_model_save_8)):
                    shutil.rmtree(best_model_dir)
                    os.mkdir(best_model_dir)
                    if (os.path.exists(BEST_NOTE)):
                        os.remove(BEST_NOTE)
                        with open(BEST_NOTE, 'a') as file6:file6.write("**********\n")
                        file6.write("训练集迭代步数："+str(step)+"    训练集的准确率"+str(train_acc)+"    训练集的损失值："+str(train_loss)+"\n")
                        file6.write("TP:" + str(TP) + "    FP:" + str(FP) + "    TN:" + str(TN) + "    FN:" + str(FN) +"\n")
                        file6.write("AR:" + str(AR) + "    TPR:" + str(TPR) + "    TNR:" + str(TNR) + "\n")
        if (os.path.exists(path_model_save_7)):
            shutil.copyfile(path_model_save_7, path_model_save_8)
            shutil.copyfile(path_model_save_1,path_model_save_2)
            shutil.copyfile(path_model_save_3,path_model_save_4)
            shutil.copyfile(path_model_save_5,path_model_save_6)
            except  tf.errors.OutOfRangeError:
            print("train--Done!!!")
            finally:
            coord.request_stop()
            coord.join(threads)
            train_writer.close()