# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:18:57 2017

@author: jackwant
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 21:54:36 2017
@author: jack
"""
import numpy as np
import cv2
import os
srcpath='./NEU_Oil/'
dstpath='./NEU_Oil/Imgs/'

for file in os.listdir(srcpath):    
    img=cv2.imread( srcpath+file) 
    if img is None: 
           continue
  
#    cv2.imshow('image',img) 
#    cv2.imshow('r',r) 
#    cv2.imshow('g',g) 
#    cv2.imshow('b',b)      
    [name, _]=  file.split('.') 
    grayname=dstpath+name+'.jpg'         
   
    cv2.imwrite(grayname,img)
     
    key=cv2.waitKey( 1)
    
cv2.destroyAllWindows()
    
    
    
          

