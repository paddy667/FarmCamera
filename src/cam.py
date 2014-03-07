#!/usr/bin/env python

from Camera import Camera
import cv2
import numpy

if __name__=="__main__":
    t = Camera()
    t.run()
    #capture = cv2.VideoCapture(0)
    #frame = capture.read()[1]
    #frameSize = frame.shape
    #print frameSize
