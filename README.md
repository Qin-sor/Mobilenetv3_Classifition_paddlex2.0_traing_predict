#  MobileNetV3 classification network based on paddlex2.0, includes training, predict --BY Q

## 1. create the env
* A conda environment is recommended, type follows code to create the same one .(NOT necessary)
```shell
conda create env -f env.yaml
```

## Prepare your dataset
* Create the folders:
```shell
mkdir train log output
```
* After making dirs, I believe you have been found the dir namely train, you should put what you want training in your prj under it , The structure is as follows:
```
- train/
    -- class1/
        -- img1
        -- img2
        -- ...
    -- class1/
        -- img1
        -- img2
        -- ...
    -- ...
        -- img1
        -- img2
        -- ...
```
* The names of the subfolders in the train folder are the names of the categories for classification, i.e., all the images in each folder correspond to a specific class.
* The names of the images in the subfolders can be arbitrary , as long as the are not repeated .

## 2. Create the train_list.txt , val_list.txt and label.txt
* Type the follow code snippets as follows:
```shell
python data_to_paddle.py
```
* After execution, train_list.txt , val_list.txt and label.txt will be generated automatically in a ratio of 8:2, You can change the ratio to any other value in the data_to_paddle.py file.

## 3. Training
* Type the follow code to training:
```shell
python train.py
```
* Other params can be changed in file namely train.py.

## Visualize
* We can type following code snippets to see training curve since we installed visualdl .
```shell
visualdl --logdir log/ --port 8080
```
* open your browser type ```localhost:8080```

## 5. predicting
* It's so easy that I can't say more details.
```shell
python predict.py
```

* Besides, Your trained model will under the folder named "output"