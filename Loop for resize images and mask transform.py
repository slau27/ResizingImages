# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:57:05 2020

@author: sharo
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import os
from os import listdir
from xml.etree import ElementTree

#os.chdir('C:/Users/slau.IASTATE.001/Desktop')
#os.chdir('C:/Users/sharo/Desktop/original')
#os.chdir('C:/Users/sharo/Desktop/reduced')

##this loop used to resize and save to new folder DONE ON MY LAPTOP
#os.getcwd()
os.chdir('C:/Users/slau.IASTATE.001/Box/Sharon Stuff/4 Factor DOE for MPI/Photos/Experiment 3 11.20.2020/Good images_cropped/')
f = os.listdir()

for i in f:
    os.chdir('C:/Users/slau.IASTATE.001/Box/Sharon Stuff/4 Factor DOE for MPI/Photos/Experiment 3 11.20.2020/Good images_cropped/')
    img = cv2.imread(i, cv2.IMREAD_UNCHANGED)
    height_orig=img.shape[0]
    width_orig = img.shape[1]
    width = 450
    height = 450
    dim = (height, width)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    os.chdir('C:/Users/slau.IASTATE.001/Box/Sharon Stuff/4 Factor DOE for MPI/Photos/Experiment 3 11.20.2020/Good images_cropped_resized_450by450/')
    cv2.imwrite(i, resized) 
    
################

os.chdir('C:/Users/sharo/Desktop/reduced')
path = 'C:/Users/sharo/Desktop/reduced'
annots_list = [f for f in os.listdir(path) if f.endswith('.xml')]

img = mpimg.imread('00016.jpg')

width = 1024
height = 1024

height_orig = img.shape[0]
width_orig = img.shape[1]

# margin allows checking alignment all corners
margin = 5

scale_width = width/width_orig
scale_height = height/height_orig

#tree = ElementTree.parse('annots/00001.xml')\
for i in annots_list:
    xml = ElementTree.parse(i)
    #tree.append(xml)
    root_each = xml.getroot()
    #root.append(root_each)# get the root of the document
    size = root_each.find('.//size')
    for box in root_each.findall('.//bndbox'):# extract each bounding box
        xmin = int(box.find('xmin').text)
        ymin = int(box.find('ymin').text)
        xmax = int(box.find('xmax').text)
        ymax = int(box.find('ymax').text)
        box_orig_pt1 = (xmin,ymin)  #  10 across,  5 down
        box_orig_pt2 = (xmax,ymax) # 500 down, 2000 across
        box.find('xmin').text = str(int(box_orig_pt1[0]*scale_width)+margin)
        box.find('ymin').text = str(int(box_orig_pt1[1]*scale_height)+margin)
        box.find('xmax').text = str(int(box_orig_pt2[0]*scale_width)-margin)
        box.find('ymax').text = str(int(box_orig_pt2[1]*scale_height)-margin)
    root_each.find('.//size/width').text = str(width)
    root_each.find('.//size/height').text = str(height)
    xml.write(i)

os.chdir('C:/Users/sharo/Desktop/original')
img = mpimg.imread('00016.jpg')
print(img)
imgplot = plt.imshow(img)
x = [1717,1903,1989,2159]
y = [1528,1603,1259,1339]
plt.imshow(img)
plt.scatter(x,y,color = 'red')
plt.show()

os.chdir('C:/Users/sharo/Desktop/reduced')
img = mpimg.imread('00016.jpg')
print(img)
imgplot = plt.imshow(img)
x = [444,482,514,547]
y = [526,542,434,452]
plt.imshow(img)
plt.scatter(x,y,color = 'red')
plt.show()
    
