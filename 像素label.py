# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 21:54:36 2017
@author: jack
"""
import numpy as np
import cv2
import os
srcpath='./NEU_SPDI/'
dstpath=srcpath+'Imgs/'
startnum=0

drawing=False
Eraser=False
Penwidth=4  
drawing = False #鼠标按下为真
def draw_circles(event,x,y,flags,param): 
    global   drawing ,Eraser,Penwidth     
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:             
            cv2.circle(imgbw,(x,y),Penwidth,255,-1)            
    elif event == cv2.EVENT_LBUTTONUP:
         drawing = False
    if event == cv2.EVENT_RBUTTONDOWN:
        Eraser = True    
    elif event == cv2.EVENT_MOUSEMOVE:
        if Eraser == True:             
            cv2.circle(imgbw,(x,y),Penwidth,0,-1)            
    elif event == cv2.EVENT_RBUTTONUP:
         Eraser = False 
now=0
for file in os.listdir(srcpath): 
    now=now+1
    if(now<startnum):
        continue
    img=cv2.imread( srcpath+file)
    if img is None: 
           continue
    print(file)    
    imgbw=img<0    
    imgbw.dtype='uint8'
    imgbw=cv2.cvtColor(imgbw,cv2.COLOR_BGR2GRAY)
    while(1):
           img2=img.copy()
           b, g, r = cv2.split(img2)
           cv2.circle(g,(10,10),Penwidth,0,-1) 
           img2=cv2.merge([b,g,imgbw])
           
           cv2.imshow('bw',imgbw) 
           cv2.imshow('image',img2)
           cv2.setMouseCallback('image',draw_circles) 
           key=cv2.waitKey(2) 
           if key== 27:
               break
           elif key == 61:
               Penwidth+=1
           elif key == 45 and Penwidth>2:
               Penwidth-=1         
#           elif key !=255:
#               print(key)     
    [name, _]=  file.split('.') 
    cv2.imwrite(dstpath+name+'.png',imgbw)
    
cv2.destroyAllWindows()
    
    
    
          
