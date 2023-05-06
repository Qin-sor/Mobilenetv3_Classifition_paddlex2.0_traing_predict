# -*- coding: utf-8 -*-
# 配置GPU
# jupyter中使用paddlex需要设置matplotlib
import matplotlib
matplotlib.use('Agg') 
# 设置使用0号GPU卡（如无GPU，执行此代码后仍然会使用CPU训练模型）
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import paddlex as pdx
import paddle


from paddlex import transforms as T

train_transforms = T.Compose(
    [T.RandomCrop(crop_size=224), T.RandomHorizontalFlip(), T.Normalize()])

eval_transforms = T.Compose([
    T.ResizeByShort(short_size=256), T.CenterCrop(crop_size=224), T.Normalize()
])

train_dataset = pdx.datasets.ImageNet(
    data_dir='./train',
    file_list='./train/train_list.txt',
    label_list='./train/label.txt',
    transforms=train_transforms,
    shuffle=True)
    
eval_dataset = pdx.datasets.ImageNet(
    data_dir='./train',
    file_list='./train/val_list.txt',
    label_list='./train/label.txt',
    transforms=eval_transforms)
    

num_classes = len(train_dataset.labels)
print("num classes = ", num_classes)
model = pdx.cls.MobileNetV3_large_ssld(num_classes=num_classes)
model.train(num_epochs=12,
            train_dataset=train_dataset,
            train_batch_size=24,
            eval_dataset=eval_dataset,
            lr_decay_epochs=[6, 8],
            save_interval_epochs=1,
            learning_rate=0.00625,
            save_dir='output/mobilenetv3_large_ssld',
            use_vdl=True)
    
