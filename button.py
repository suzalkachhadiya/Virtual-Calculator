import cv2
import streamlit as st
from cvzone.HandTrackingModule import HandDetector

class Button:
    def __init__(self,pos,width,height,value):
        self.pos=pos
        self.width=width
        self.height=height
        self.value=value

    def draw(self,img):
        cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),
                      (225,225,255),cv2.FILLED)
        cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),
                      (45,45,45),3)
        cv2.putText(img,self.value,(self.pos[0]+33,self.pos[1]+50),cv2.FONT_HERSHEY_PLAIN,
                    2,(0,0,0),2)
        
    def checkClick(self,x,y):
        if self.pos[0] < x < self.pos[0]+self.width and \
                self.pos[1] < y < self.pos[1]+self.height:
            cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),
                      (225,225,255),cv2.FILLED)
            cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),
                        (45,45,45),3)
            cv2.putText(img,self.value,(self.pos[0]+15,self.pos[1]+70),cv2.FONT_HERSHEY_PLAIN,
                        5,(0,0,0),5)
            return True
        return False
