import marker_function as mf
import human_function as hf
import cv2
import numpy


class Distance:
    def __init__(self,json_path,img_path):
        self.img = cv2.imread(img_path)
        self.m1 = mf.Marker(img_path)
        self.j1 = hf.includeJson(json_path)

        human_points = self.j1.makeGroundPoint()

        u1, v1 = self.m1.chair_u_v() 
        self.u_chair,self.v_chair = round(u1),round(v1)
        u2 , v2 = self.m1.cal_u_v(human_points[0],human_points[1])
        self.u_human ,self.v_human = round(u2), round(v2)
   
    """
    def write_distance (self):
        u_c = round(self.u_chair)
        v_c = round(self.v_chair)
        u_h = round(self.u_human)
        v_h = round(self.v_human)
        cv2.line(self.img, (u_c,v_c),(u_h,v_h), (0,255,0))
    """

    def show_image(img_path):
        #img = cv2.imread(img_path)
        cv2.imshow('Img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def getChair (self):
        return (self.m1.region_chair)

    def getHuman (self):
        return (self.j1.makeGroundPoint())

    def getPosition (self):
        return ((self.getChair(),self.getHuman()))

    def write_distance (self):
        p1,p2 = self.getPosition ()
        cv2.line(self.img,(100,200), (200,300), (0,255,0),6)
        main.show_image(self.img)

    def cal_distance (self):
        distance = pow((self.u_human-self.u_chair)**2 + (self.v_human-self.v_chair)**2,0.5)
        return distance
    




