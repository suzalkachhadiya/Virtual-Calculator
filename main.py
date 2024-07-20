import cv2
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

cap=cv2.VideoCapture(0)
cap.set(3,1080) # width
cap.set(4,480) # height
detector=HandDetector(detectionCon=0.7, maxHands=1)

buttonValues=[['(',')','E','C'],
              ['7','8','9','*'],
              ['4','5','6','+'],
              ['1','2','3','-'],
              ['0','.','=','/'],]

buttonnList=[]
for i in range(4):
    for j in range(5):
        xpos=i*100 + 500
        ypos=j*100 + 190
        buttonnList.append(Button((xpos,ypos),80,80,buttonValues[j][i]))

#varables
myEquation=""
delayCounter=0

while True:
    try:
        #get image from webcam
        success, img= cap.read()

        if not success:
                print("Error: Failed to read frame from webcam.")
                break
        
        img=cv2.flip(img, 1)

        #Detection of hand
        hands, img=detector.findHands(img,flipType=False)

        # Draw all button
        cv2.rectangle(img,(500,50),(500+383,80+80),
                        (225,225,255),cv2.FILLED)
        cv2.rectangle(img,(500,50),(500+383,80+80),
                        (45,45,45),3)
        for button in buttonnList:
            button.draw(img)

        # chech for hand
        if hands:
            lmlist=hands[0]['lmList']
            length, _, img = detector.findDistance(lmlist[8][:2],lmlist[12][:2],img)
            # print(length)
            x,y=lmlist[8][:2]
            if length<50:
                for i, button in enumerate(buttonnList):
                    if button.checkClick(x,y) and delayCounter==0:
                        myValues=buttonValues[int(i%5)][int(i/5)]
                        print(i,"->",myValues)
                        if myValues== "=":
                            myEquation=str(eval(myEquation))
                        elif myValues=="E":
                            myEquation=myEquation[:-1] if myEquation else myEquation
                            # print(myEquation)
                        elif myValues=="C":
                            myEquation=""
                        else:
                            myEquation+=myValues
                        delayCounter=1
        
        # Avoid Duplicates
        if delayCounter!=0:
            delayCounter+=1
            if delayCounter>10:
                delayCounter=0

        # Display the result / equation
        cv2.putText(img,myEquation,(510,120),cv2.FONT_HERSHEY_PLAIN,
                        3,(40,40,40),3)

        #display Image
        cv2.imshow("Image",img)
        cv2.waitKey(1)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        break