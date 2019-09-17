#!/usr/bin/env python
# coding: utf-8

# ## Increase Image Contrast

# In[2]:


#cerner_2^5_2019
import cv2
from matplotlib import pyplot as plt

def increaseImageContrast(imagePath, fileName):
    filePath = imagePath + fileName
    img = cv2.imread(filePath, 1)
    plt.imshow(img)
    plt.title(fileName)
    plt.axis('off')
    plt.show()
    
    # CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=3., tileGridSize=(8,8))

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
    l, a, b = cv2.split(lab)  # split on 3 different channels

    l2 = clahe.apply(l)  # apply CLAHE to the L-channel

    lab = cv2.merge((l2,a,b))  # merge channels
    img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR
    plt.imshow(img2)
    plt.title('Modified_' + fileName)
    plt.axis('off')
    plt.show()
    
imagePath = 'Images\\'
fileName1 = 'image101.jpg'
increaseImageContrast(imagePath, fileName1)

