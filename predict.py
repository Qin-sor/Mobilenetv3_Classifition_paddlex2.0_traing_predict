import os
root_dir = "/home/nuvo/QHL/datasets/长通数据/前45度"
import paddlex as pdx
model = pdx.load_model('output/mobilenetv3_large_ssld/best_model')

image_name = "/home/nuvo/QHL/deep_learning/QHL_finall_test_color/data_to_predict/1.jpg"
result = model.predict(image_name,topk=1)
print("Predict Result:", result)

'''
car_num = []
path = r'/home/nuvo/QHL/datasets/长通数据/前45度'  # 文件目录 
for root, dir, files in os.walk(path):
        for i in range(len(files)):
            print("现在开始检测： ", files[i])
            a = [test_one4(path+files[i]), files[i]]
            car_num.append(a)
        
print(len(car_num))
for i in range(len(car_num)):
    print(car_num[i], end= '\n')
'''
