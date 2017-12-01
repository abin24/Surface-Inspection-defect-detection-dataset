# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 09:56:18 2017

@author: jackwant
"""
 
import numpy as np
import cv2
import os 
 
for i in range(1,11):
    srcpath='./DGAM_Class'+str(i)+'/Test/'
    for file in os.listdir(srcpath):  
       
       img=cv2.imread( srcpath+file)        
       if img is None: 
           continue
       [name, _]=  file.split('.')
       labelname=srcpath+"Label/"+name+'_label.PNG'
       imgl=cv2.imread( labelname)
       b, g, r = cv2.split(img)
       imgSave='./DGAM_Test/DGAM_Test_Class'+str(i)+'/Imgs/'+name
       if imgl is None: 
           label=r-b
         
       else:
          
         
           b2, g2, r2 = cv2.split(imgl)
           label=b2
           img=cv2.merge([b2,g,r])
         
#       cv2.imshow('image',img)
#       cv2.imshow('label',label)   
       cv2.imwrite(imgSave+'.jpg',r)
       cv2.imwrite(imgSave+'.png',label)
       if imgl is None:
           cv2.waitKey( 1)
       else:               
          cv2.imwrite(imgSave+'.bmp',img)
       
       key=cv2.waitKey( 1)
    
cv2.destroyAllWindows()
    
    
    
          

