import json

class includeJson:
    def __init__(self,json_path):
        with open(json_path) as f:
            df = json.load(f)
        self.pose = df["people"][0]["pose_keypoints_2d"]

    """
    def extractJson(self):
        json_num = "1"
        root_path = "images/walk1/"
        json_root_path = "walk1_json/"
        json_path = root_path + json_root_path + "walk1_00000000000" + json_num +"_keypoints.json"
        json = includeJson(json_path)
        result = json.makeBoundingBox()
        print (result)
    """

    def extract_joints (self,l) :
        length = len(l)
        res = []
        for i in range (length):
            if i % 3 == 0:
                x = l[i]
            if i % 3 == 1:
                y = l[i]
            if i % 3 == 2:
                per = l[i]
                res.append([x,y,per])
        return res

    def make_jointX (self,l):
        res = []
        for item in l:
            res.append(item[0])
        return res

    def make_jointY (self,l):
        res = []
        for item in l:
            res.append(item[1])
        return res

    def makeBoundingBox(self):
        joints = self.extract_joints(self.pose)
        joint_x = self.make_jointX (joints)
        joint_y = self.make_jointY (joints)
        joint_x_R0 = self.remove_0(joint_x)
        joint_y_R0 = self.remove_0(joint_y)
        x = round (max (joint_x_R0))
        w = round (min (joint_x_R0))
        y = round (max (joint_y_R0))
        h = round (min (joint_y_R0))
        return ((x,y,w,h))

    def remove_0(self,l):
        result = []
        for item in l:
            if item == 0:
                None
            else :
                result.append (item)
        return (result)

    def makeGroundPoint (self):
        x,y,u,v = self.makeBoundingBox()
        human_points = ((x + u)/2, y)
        return (human_points)
    
    