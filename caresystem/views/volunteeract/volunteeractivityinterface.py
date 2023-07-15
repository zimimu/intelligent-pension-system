# 导入包
from caresystem.views.oldcare.facial import FaceUtil
from scipy.spatial import distance as dist
from caresystem.views.oldcare.utils import fileassistant
from caresystem.views.dataManage import addEvent
from PIL import Image, ImageDraw, ImageFont
import cv2
import time
import imutils
import numpy as np

# 全局变量
pixel_per_metric = None
model_path = 'caresystem/views/models/face_recognition_hog.pickle'
people_info_path = 'caresystem/views/info/people_info.csv'

# 全局常量
FACE_ACTUAL_WIDTH = 20  # 单位厘米   姑且认为所有人的脸都是相同大小
VIDEO_WIDTH = 640
VIDEO_HEIGHT = 480
ACTUAL_DISTANCE_LIMIT = 100  # cm

# 得到 ID->姓名的map 、 ID->职位类型的map
id_card_to_name, id_card_to_type = fileassistant.get_people_info(people_info_path)
faceutil = FaceUtil(model_path)
insert = 0
activity_timing = 0
activity_start_time=0
activity_limit_time=1

def volunteeractivity(grabbed, frame):
    global insert,activity_limit_time,activity_timing,activity_start_time
    if not grabbed:
        return
    frame = imutils.resize(frame,
                           width=VIDEO_WIDTH,
                           height=VIDEO_HEIGHT)  # 压缩，加快识别速度

    face_location_list, names = faceutil.get_face_location_and_name(
        frame)

    people_type_list = list(set([id_card_to_type[i] for i in names]))

    volunteer_centroids = []
    old_people_centroids = []
    old_people_name = []

    # loop over the face-bounding boxes
    for ((left, top, right, bottom), name) in zip(face_location_list,
                                                  names):  # 处理单个人

        person_type = id_card_to_type[name]
        # 将人脸框出来
        rectangle_color = (0, 0, 255)
        if person_type == 'old_people':
            rectangle_color = (0, 0, 128)
        elif person_type == 'employee':
            rectangle_color = (255, 0, 0)
        elif person_type == 'volunteer':
            rectangle_color = (0, 255, 0)
        else:
            pass
        cv2.rectangle(frame, (left, top), (right, bottom),
                      rectangle_color, 2)

        if 'volunteer' not in people_type_list:  # 如果无义工则跳出循环
            continue

        if person_type == 'volunteer':  # 如果检测到有义工存在
            # 获得义工位置
            volunteer_face_center = (int((right + left) / 2),
                                     int((top + bottom) / 2))
            volunteer_centroids.append(volunteer_face_center)

            cv2.circle(frame,
                       (volunteer_face_center[0],
                        volunteer_face_center[1]),
                       8, (255, 0, 0), -1)

        elif person_type == 'old_people':  # 如果没有发现义工
            old_people_face_center = (int((right + left) / 2),
                                      int((top + bottom) / 2))
            old_people_centroids.append(old_people_face_center)
            old_people_name.append(name)

            cv2.circle(frame,
                       (old_people_face_center[0],
                        old_people_face_center[1]),
                       4, (0, 255, 0), -1)
        else:
            pass

        # 把人名写上(同时处理中文显示问题)
        img_PIL = Image.fromarray(cv2.cvtColor(frame,
                                               cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_PIL)
        final_label = id_card_to_name[name]
        draw.text((left, top - 30), final_label,
                  font=ImageFont.truetype(r'msyh.ttc', 40), fill=(255, 0, 0))  # linux
        # 转换回OpenCV格式
        frame = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)

    # 在义工和老人之间划线
    for i in volunteer_centroids:
        for j_index, j in enumerate(old_people_centroids):
            pixel_distance = dist.euclidean(i, j)
            face_pixel_width = sum([i[2] - i[0] for i in
                                    face_location_list]) / len(face_location_list)
            pixel_per_metric = face_pixel_width / FACE_ACTUAL_WIDTH
            actual_distance = pixel_distance / pixel_per_metric

            if actual_distance < ACTUAL_DISTANCE_LIMIT:
                cv2.line(frame, (int(i[0]), int(i[1])),
                         (int(j[0]), int(j[1])), (255, 0, 255), 2)
                label = 'distance: %dcm' % (actual_distance)
                cv2.putText(frame, label, (frame.shape[1] - 150, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 0, 255), 2)

                if activity_timing == 0:  # just start timing
                    activity_timing = 1
                    activity_start_time = time.time()
                else:  # already started timing
                    activity_end_time = time.time()
                    difference = activity_end_time - activity_start_time
                current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                if difference < activity_limit_time:
                    print("忽略")
                else:  # he/she is really smiling
                    # insert into database
                    if (insert == 0):
                        # 插入数据库
                        print("交互")
                        addEvent(id,'互动','房间')
                        insert = 1
            else:
                insert = 0
                activity_timing = 0

    # show our detected faces along with smiling/not smiling labels
    return frame
