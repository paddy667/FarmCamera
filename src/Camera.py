#!/usr/bin/env python

import cv2
import numpy as np



def diffFrames(f0,f1,f2):
    diff1 = cv2.absdiff(f2, f1)
    diff2 = cv2.absdiff(f1,f0)
    return cv2.bitwise_and(diff1, diff2)
    
    
class Camera:
    
    
    def __init__(self):
        # Capture video from camera
        self.capture = cv2.VideoCapture(0)
    
    def run(self):
        videoFrame = self.capture.read()[1]
        videoFrameSize = videoFrame.shape
        
        blank_image = np.zeros(videoFrameSize, np.uint8)
        
        
        
        gFrameMinus = cv2.cvtColor(self.capture.read()[1], cv2.COLOR_RGB2GRAY)
        gFrame = cv2.cvtColor(self.capture.read()[1], cv2.COLOR_RGB2GRAY)
        gFramePlus = cv2.cvtColor(self.capture.read()[1], cv2.COLOR_RGB2GRAY)
        

        while True:
            
            #cv2.imshow("Camera", diffFrames(gFrameMinus, gFrame, gFramePlus))
            
            cv2.imshow("Camera1",blank_image)
            #cv2.imshow("Camera2",gFramePlus)
            
            gFrameMinus = gFrame
            gFrame = gFramePlus
            gFramePlus = cv2.cvtColor(self.capture.read()[1], cv2.COLOR_RGB2GRAY)
            
            
        
            # Listen for ESC key
            c = cv2.waitKey(7) % 0x100
            if c == 27:
                break

        

