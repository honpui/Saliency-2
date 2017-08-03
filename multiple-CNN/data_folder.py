import os
import glob
import numpy as np
import shutil



def folder_generator(filenames):
    train_list = []
    test_list = []
    val_list = []
    os.makedirs(os.path.join(PATH, 'train'), exist_ok=True)
    os.makedirs(os.path.join(PATH, 'test'), exist_ok=True)
    os.makedirs(os.path.join(PATH, 'val'), exist_ok=True)
    for name in filenames:
        tmp = name.split('_')
        if tmp[1] == 'test2014':
            shutil.move(name, TEST_PATH)
        elif tmp[1] == 'train2014':
            shutil.move(name, TRAIN_PATH)
        else:
            shutil.move(name, VAL_PATH)

if __name__ == '__main__':

    DATASET_NAME = "COCO"
    PATH = "/home/lei/Images/COCO"
    TRAIN_PATH = os.path.join(PATH, 'train')
    TEST_PATH = os.path.join(PATH, 'test')
    VAL_PATH = os.path.join(PATH, 'val')

    filenames =  glob.glob(PATH + '/*.jpg')

    folder_generator(filenames)
