import cv2
import numpy as np
import marker_function as mf
import human_function as hf
from distance import Distance

project_name = "walk1"



def show_image(img_path):
    #img = cv2.imread(img_path)
    cv2.imshow('Img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def make_path(json_root,img_root,json_num):
    img_num = json_num + 1
    if json_num < 9:
        json_path = json_root + project_name + "_00000000000" + "{}_".format(json_num) + "keypoints.json"
        img_path = img_root + "00000" + "{}".format(img_num) + ".png"
    elif json_num == 9:
        json_path = json_root + project_name + "_00000000000" + "{}_".format(json_num) + "keypoints.json"
        img_path = img_root + "0000" + "{}".format(img_num) + ".png"
    elif 9 < json_num and json_num < 99 :
        json_path = json_root + project_name + "_0000000000" + "{}_".format(json_num) +"keypoints.json"
        img_path = img_root + "0000" + "{}".format(img_num) + ".png"
    elif json_num == 99:
        json_path = json_root + project_name + "_0000000000" + "{}_".format(json_num) +"keypoints.json"
        img_path = img_root + "000" + "{}".format(img_num) + ".png"
    elif 99 < json_num and json_num < 999:
        json_path = json_root + project_name + "_000000000" + "{}_".format(json_num) +"keypoints.json"
        img_path = img_root + "000" + "{}".format(img_num) + ".png"
    else:
        json_path = json_root + project_name + "_00000000" + "{}_".format(json_num) + "keypoints.json"
        img_path = img_root + "000" + "{}".format(img_num) + ".png"
    return (json_path,img_path)


def make_path_from_json_num(json_num):
    json_root = "images/{}/{}_json/".format(project_name,project_name) 
    img_root = "images/{}/{}_png/".format(project_name,project_name) 
    json_path, img_path = make_path(json_root,img_root,json_num)
    return (json_path,img_path)

def movie_test (movie_path):
    delay = 1
    window_name = 'frame'

    cap = cv2.VideoCapture(movie_path)

    if not cap.isOpened():
        sys.exit()

    while True:
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (0, 0), 5)
            cv2.imshow(window_name, blur)
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    cv2.destroyWindow(window_name)

def show_movie (movie_path):
    delay = 1
    window_name = 'frame'

    cap = cv2.VideoCapture(movie_path)

    if not cap.isOpened():
        sys.exit()

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow(window_name, blur)
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    cv2.destroyWindow(window_name)




def do_once (frame_num):
    json_path,img_path = make_path_from_json_num (frame_num)
    dis = Distance(json_path,img_path)
    distance = dis.cal_distance()
    dis.write_distance()
    return (distance)


if __name__ == '__main__':
    """ movie version
    movie_path = "images/walk1/walk1.mp4"
    movie (movie_path)
    """
    """ folder version
    res = []
    for i in range(359):
        res.append(do_once (i))
    print (res)
    """
    do_once (1)

""""
cv2.rectangle(img, (458, 670), (467, 673), (255, 255, 0))
cv2.rectangle(img, (467, 646), (477, 648), (255, 255, 0))
cv2.rectangle(img, (478, 624), (486, 626), (255, 255, 0))
cv2.rectangle(img, (540, 665), (551, 667), (255, 255, 0))
cv2.rectangle(img, (543, 641), (552, 643), (255, 255, 0))
cv2.rectangle(img, (548, 621), (556, 623), (255, 255, 0))
cv2.rectangle(img, (622, 661), (633, 663), (255, 255, 0))
cv2.rectangle(img, (619, 638), (626, 640), (255, 255, 0))
cv2.rectangle(img, (616, 615), (624, 620), (255, 255, 0))
"""
"""
    marker location
    marker_all = img[600:700,450:650] #about
    marker_1 = img[670:673,458:467] => rec( (458,670), (467,673) ) ok
    marker_2 = img[646:648,467:477] => rec( (467,646), (477,648) ) ok
    marker_3 = img[624:626,478:486] => rec( (478,624), (486,626) ) ok
    marker_4 = img[665:667,540:551] => rec( (540,665), (551,667) ) ok
    marker_5 = img[641:643,543:552] => rec( (543,641), (552,643) ) ok
    marker_6 = img[621:623,548:556] => rec( (548,621), (556,623) ) ok
    marker_7 = img[661:663,622:633] => rec( (622,661), (633,663) ) ok
    marker_8 = img[638:640,619:626] => rec( (619,638), (626,640) ) ok
    marker_9 = img[615:620,616:624] => rec( (616,615), (624,620) ) ok
    img [x1:x2,y1:y2] => rec((y1,x1),(y2,x2))
    """
