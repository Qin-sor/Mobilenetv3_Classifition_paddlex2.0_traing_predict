# -*- coding: utf-8 -*-
import os, shutil
all_type_name = []

#这里是已经按照文件夹对应名称放好的状态
#制作label
def write_label(rootDir):
    #写入文件夹
    f = open('label.txt', 'w')
    filenames = os.listdir(rootDir)
    filenames.sort()
    for filename in filenames:
        all_type_name.append(filename)
    #排序
    all_type_name.sort()
    for filename in all_type_name:
        f.write(filename+'\n')
    f.close()

#制作train.txt和test.txt
def write_test_txt():
    test_final_idx = 0
    f_train = open('train_list.txt', 'w')
    f_val = open('val_list.txt', 'w')
    type_num = -1
    for i in all_type_name:
        type_num = type_num + 1
        #到每个文件夹
        pathname = os.path.join(root_path,i)
        list_files = os.listdir(pathname)

        if len(list_files)==2:              #划分测试集
            test_final_idx = 0
        else:
            test_final_idx = round(len(list_files)*0.8)
        #迭代指数
        tmp_file_idx = 0
        #到每个文件
        for j in list_files:
            if tmp_file_idx < test_final_idx :
                f_train.write(os.path.join(pathname, j) +' '+ str(type_num) +'\n')
            else:
                f_val.write(os.path.join(pathname, j) +' '+ str(type_num) +'\n')
            tmp_file_idx = tmp_file_idx + 1
    f_train.close()
    f_val.close()
            # print(list_file)  在这里是完全正确的路径

#打乱
def shuffle_file(file_name):
    import random
    all_lines = []
    for line in open(file_name):
        all_lines.append(line)
    random.shuffle(all_lines)
    f = open(file_name, 'w')
    for line in all_lines:
        f.write(line)
    f.close()

#顺序执行才可以
root_path = "/home/nuvo/QHL/deep_learning/QHL_Paddlex_Mobilenetv3_Classifition/train"  #用绝对路径,指引到train文件夹
write_label(root_path)
write_test_txt()
#打乱写入
shuffle_file(file_name="train_list.txt")
shuffle_file(file_name="val_list.txt")
#移动文件
shutil.move("train_list.txt", "train/")
shutil.move("val_list.txt", "train/")
shutil.move("label.txt", "train/")

