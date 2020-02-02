import cv2 
import numpy as np
import numpy.linalg as LA

class Marker:
    def __init__(self,img):
        #(x,y):marker_real_point
        self.m_real = [(0,0),(0,30),(0,60),
                       (30,0),(30,30),(30,60),
                       (60,0),(60,30),(60,60)]
        
        #(u1,v1),(u2,v2): 
        self.marker_list = [((458, 670), (467, 673)), ((467, 646), (477, 648)), ((478, 624), (486, 626)),
                            ((540, 665), (551, 667)), ((543, 641), (552, 643)), ((548, 621), (556, 623)),
                            ((622, 661), (633, 663)), ((619, 638), (626, 640)), ((616, 615), (624, 620))]
        
        # region of chair: (u1,v1),(u2,v2)
        self.region_chair = ((582,420),(670,540))
        self.img = img

    def chair_u_v(self):
        x = (self.region_chair [0][0] + self.region_chair[1][0])/ 2
        y = (self.region_chair [0][1] + self.region_chair[1][1])/ 2
        return (self.cal_u_v(x,y))



    def write_marker (self):
        for item in self.marker_list:
            cv2.rectangle(self.img, item[0], item[1], (255, 255, 0))
    
    def cal_ave (self):
        res = []
        for item in self.marker_list:
            x = (item[0][0] + item[1][0]) / 2
            y = (item[0][1] + item[1][1]) / 2
            res.append((x, y))
        return res

    def write_chair (self):
        cv2.rectangle(self.img, self.region_chair[0],self.region_chair[1], (0, 255, 255))

    def write_region (self):
        self.write_marker()
        self.write_chair()
        
    def cal_consts(self):
        delta = []
        result_x = []
        result_z = []
        result_alpha = []
        result_beta = []
        minus_ones = [-1,-1,-1,-1,-1,-1,-1,-1]

        ave_mrk = self.cal_ave()
        for x,y in ave_mrk :
            delta.append(x + y)
        delta = np.array(delta[:8])

        for i in range(8):
            x = delta[i] * self.m_real[i][0]
            y = delta[i] * self.m_real[i][1]
            result_alpha.append(x)
            result_beta.append(y)
            result_x.append(self.m_real[i][0])
            result_z.append(self.m_real[i][1])
        
        A = np.array ([result_alpha,result_beta,result_x,result_z,minus_ones,result_x,result_z,minus_ones])

        det = LA.det(A)
        A_inv = LA.pinv(A)
        C = A_inv @ delta.T
        return C

    def cal_u_v (self,x,y):
        c = self.cal_consts()
        a_1 = c[6] - c[4] * c[7] 
        a_2 = c[0] - c[2] * c[3]
        a_3 = c[2] * c[5] - c[0] * c[7]
        a_4 = c[3] * c[7] -c[5] 
        a_5 = c[0] - c[2] * c[3]
        a_6 = c[2] * c[5] - c[0] * c[7]
        A = (c[4] * c[5] - c[3] * c[6]) * x + (c[1] * c[3] -c[0] * c[4]) * y + (c[0] * c[6] - c[1] * c[5])
        u = (a_1 * x + a_2 * y + a_3) / A
        v = (a_4 * x + a_5 * y + a_6) / A
        return (u,v)

