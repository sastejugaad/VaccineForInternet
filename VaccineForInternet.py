#Relax Bro its just 40 lines
#Install following Libraries
#If you get any error GOOGLE IT FIRST
# Import required packages
import numpy as np
import cv2 
import pytesseract 
from PIL import ImageGrab
import os
import time
# Mention the installed location of Tesseract-OCR in your system 

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'# Provide correct path for tesseract

fourcc = cv2.VideoWriter_fourcc('X','V','I','D') #you can use other codecs as well.
vid = cv2.VideoWriter('record.avi', fourcc, 8, (800,490)) #change numbrs here to resize the capture window

while(True):
    
    img = ImageGrab.grab(bbox=(100, 10, 800, 500)) #x, y, w, h
    img_np = np.array(img)

    hImg,wImg,_ = img_np.shape
    #cong = r'--oem 3 --psm 6 outputbase digits'
    boxes = pytesseract.image_to_data(img_np) #,config=cong
    for x,b in enumerate(boxes.splitlines()):
        #print(b)
        if x!=0:            
            b = b.split()            
        if len(b)==12:      
            #print(b[11])
            if b[11] in ['TikTok','tik tok','tiktok','Tik Tok','Roast','ROAST','roast','CRINGE','cringe','reaction','REACTION']:
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.rectangle(img_np,(x,y),(w+x,h+y),(0,0,255),3)
                #Uncomment line bleow to close the browser
                #You can add any application you like.
                os.system("TASKKILL /F /IM firefox.exe")
                cv2.putText(img_np,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

    cv2.imshow('Result',img_np)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    
cv2.destroyAllWindows()       
vid.release()

#bus ho gaya kaam maje karo frands
 

    
    
