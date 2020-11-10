import os
import numpy as np

def get_files_test(filename):
    class_train = []
    label_train = []
    for train_class in os.listdir(filename):
        for pic in os.listdir(filename+train_class):
            class_train.append(filename+train_class+'\\'+pic)
            label_train.append(train_class)
    temp = np.array([class_train,label_train])
    temp = temp.transpose()               #将temp进行转置
    #np.random.shuffle(temp)             #将temp打乱顺序
    #after transpose, images is in dimension 0 and label in dimension 1
    image_list = list(temp[:,0])
    label_list = list(temp[:,1])
    label_list = [int(i) for i in label_list]
#把label_list中的元素统一转换为Int类型
    return image_list,label_list