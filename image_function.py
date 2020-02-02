import cv2
import random

class mouseParam:
    def __init__(self,input_img_name):
        self.mouseEvent = {"x":None,"y":None,"event":None,"flags":None}
        cv2.setMouseCallback(input_img_name,self.__CallBackFunc,None) 


    def __CallBackFunc (self, eventType, x, y, flags, userdata):
        self.mouseEvent["x"] = x
        self.mouseEvent["y"] = y
        self.mouseEvent["event"] = eventType
        self.mouseEvent["flags"] = flags

    def getData (self):
        return self.mouseEvent
    
    def getEvent (self):
        return self.mouseEvent["event"]

    def getFlags(self):
        return self.mouseEvent["flags"]
    
    def getX(self):
        return self.mouseEvent["x"]
    
    def getY(self):
        return self.mouseEvent["y"]

    def getPosition(self):
        return (self.mouseEvent["x"],self.mouseEvent["y"])

def end_pos():
    if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN:
        ps = mouseData.getPosition()
        print (ps)
        print ("End Position is saved: {}".format(ps))
        return ps

if __name__ == "__main__":
    img_path = 'images/marker_Moment.jpg' 
    read = cv2.imread(img_path)
    original_read = cv2.imread(img_path)
    win_name = "input window"
    cv2.imshow(win_name,read)
    mouseData = mouseParam(win_name)
    sps = None
    eps = None
    res = []

    while 1:
        k = cv2.waitKey(20) &0xff
        if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN:
                sps = mouseData.getPosition()
                print ("Start Position is saved: {}".format(sps))
            
        elif mouseData.getEvent() == cv2.EVENT_RBUTTONDOWN:
                eps = mouseData.getPosition()
                print ("Start Position is saved: {}".format(eps))
            
        elif k == ord ('d'):
            rand_g = random.randrange(255)
            rand_b = random.randrange(255)
            rand_r = random.randrange(255)
            cv2.rectangle(read, sps, eps, (rand_g, rand_b, rand_r))
            cv2.imshow(win_name, read)
            print ("start: {}, end: {}".format(sps,eps))
            res.append((sps,eps))

        elif k == ord ('c'):
            cv2.destroyWindow(win_name)
            res = []
            read = original_read 
            cv2.imshow(win_name,read)
            mouseData = mouseParam(win_name)
            print ("reboot window")


        elif k == 27:
            cv2.destroyAllWindows()
            break;
    print (res)
    print("Finished")
