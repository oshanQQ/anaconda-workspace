from tkinter import image_names
import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

def mirror_padding(img_path):
    img1 = cv2.imread(img_path)
    padding_y = img1.shape[0] // 10
    padding_x = img1.shape[1] // 10
    img2 = cv2.copyMakeBorder(img1, padding_y, padding_y, padding_x, padding_x, cv2.BORDER_REFLECT_101)
    return img2    

image_paths = glob.glob('./training_images/*')
for image_path in image_paths:
    img_name = image_path.split('/')[-1]
    img = mirror_padding(image_path)
    cv2.imwrite('./converted_train_images/' + img_name, img)


