import math
import datetime
import dlib
from caresystem.views.intrusiondetection.object_detection import ObjectDetection  # 导入定义好的目标检测方法
import numpy as np
import cv2
from multiprocessing import Queue
import threading
# from copy import deepcopy

# import pymssql

thread_lock = threading.Lock()
thread_exit = False
# db = pymssql.connect('LAPTOP-BEOF4ADA', 'sa', 'st13534351140', 'owl', charset='utf8')
# cur = db.cursor()
# filepath ='rtmp://47.93.4.51:1935/live/stream' # "D:\Test_vedio\F_people.avi"'rtmp://47.93.4.51:1935/live/stream'
filepath = 0 # 表示调用本地摄像头
cap = cv2.VideoCapture(filepath)
cap.set(6, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
# cap.set(3, 480)
# cap.set(4, 640)
cap.set(3, 500)
cap.set(4, 400)
print(cap.get(5))

x1=0
y1=0
# x2 = int(cap.get(3))
# y2 = int(cap.get(4))
x2 = 500
y2 = 400
print("x2，y2:")
print(x2,y2)
od = ObjectDetection()
all_r=[]
#写入侵数据
# def save(a):
#     if len(a)>0:
#         day=str(a[0].year)+"-0"+str(a[0].month)+"-"+str(a[0].day)
#         addr=str(a[0].day) + str(a[0].hour) +str(a[0].minute) + str(a[0].second)
#         start= str(a[0].hour) +":"+ str(a[0].minute) + ":"+str(a[0].second)
#         end=str(a[2].hour) + ":"+str(a[2].minute) + ":"+str(a[2].second)
#         sql="""insert into rec_vedio values ('%s','%s','%d','%s','%s',NULL)"""%(day,start,a[1],end,addr)
#         cur.execute(sql)
#         db.commit()
#         print("s")

class myThread(threading.Thread):
    def __init__(self,  img_height, img_width):
        super(myThread, self).__init__()
        # self.img_height = img_height
        # self.img_width = img_width
        self.img_height = 500
        self.img_width = 600
        self.frame = np.zeros((img_height, img_width, 3), dtype=np.uint8)

    def stop(self):
        thread_exit = False
    #
    # def __del__(self):
    #     self.out.release()
    #

    def run(self):
        global thread_exit
        while not thread_exit:
            ret, frame = cap.read()
            if ret:
                frame = cv2.resize(frame, (self.img_width, self.img_height))
                self.frame = frame
                global q
                q.put(frame)
            else:
                thread_exit = True
        cap.release()

def deal_v():
    global thread_exit
    global q
    q=Queue()
    # camera_id ='rtmp://47.93.4.51:1935/live/stream'#"D:\Test_vedio\yb2.mp4"
    # img_height = int(cap.get(4))
    # img_width = int(cap.get(3))
    img_height = 500
    img_width = 600
    thread = myThread(img_height, img_width)
    thread.start()
    # w = int(cap.get(4))
    # h = int(cap.get(3))
    w = 500
    h = 400
    trackers_ = []
    labels = []
    stay=[]
    end_time=''
    start_time=''
    total_people = 0
    vedio_tag = 0
    start_id = 0
    end_id = 0
    count = 0
    box_len = 0
    center_tracker = []  # 追踪器的中心点

    while True:
        # thread_lock.acquire()
        a1 = x1
        b1 = y1
        a2 = x2
        b2 = y2
        img_origin = q.get()
        count += 1  # 记录当前是第几帧
        # print('------------------------')
        # print('NUM:', count)
        # print("画框")
        if img_origin is None:
            break
        # （1）读取视频
        img = img_origin
        roi = img_origin[b1:b2, a1:a2]
        img = roi
        # （2）画框
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # （4）识别
        if count % 50 == 1:
            print("识别")
            # （4）目标检测
            class_ids, scores, boxes = od.detect(img)
            print(class_ids)
            if len(boxes)==0:
                trackers_.clear()
                labels.clear()
                stay.clear()
            if box_len == 0:
                for box, p in zip(boxes, class_ids):
                    if p == 0:
                        # 一个人的中心点
                        (x, y, w, h) = box
                        # 使用dlib来进行目标追踪
                        t = dlib.correlation_tracker()
                        rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
                        t.start_track(rgb, rect)
                        total_people = total_people + 1
                        # 保存结果
                        labels.append(total_people)
                        trackers_.append(t)
                        stay.append(count)
            else:
                for box, p in zip(boxes, class_ids):
                    if p == 0:
                        # 一个人的中心点
                        (x, y, w, h) = box
                        # 获取每一个框的中心点坐标，像素坐标是整数
                        cx, cy = int((x + x + w) / 2), int((y + y + h) / 2)
                        add_state = 1
                        for t_center in center_tracker:
                            distance = math.hypot(t_center[0] - cx, t_center[1] - cy)
                            # print(distance)
                            if distance < 300:  # 像素差
                                add_state = 0
                        if add_state == 1:
                            # print("add")
                            # 使用dlib来进行目标追踪
                            t = dlib.correlation_tracker()
                            rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
                            t.start_track(rgb, rect)
                            total_people = total_people + 1
                            # 保存结果
                            labels.append(total_people)
                            trackers_.append(t)
                            stay.append(count)

        box_len = len(center_tracker)
        now = []

        for (t, id,s) in zip(trackers_, labels,stay):
            t.update(rgb)
            pos = t.get_position()
            # 得到位置
            startX = int(pos.left())
            startY = int(pos.top())
            endX = int(pos.right())
            endY = int(pos.bottom())
            print(endX)
            print(endY)
            if startX <= 0 or startY <= 0 or endX >= a2 - a1 or endY >= b2 - b1:
                trackers_.remove(t)
                labels.remove(id)
                stay.remove(s)
                continue
            # 获取每一个框的中心点坐标，像素坐标是整数
            t_cx, t_cy = int((startX + endX) / 2), int((startY + endY) / 2)
            if count-s>750:
                cv2.rectangle(img, (startX, startY), (endX, endY), (255, 0, 0), 2)
                cv2.putText(img, str("waring!!"), (t_cx, t_cy), 0, 1, (0, 0, 255), 2)
            else:
                now.append((t_cx, t_cy))
                cv2.circle(img, (t_cx, t_cy), 5, (255, 0, 0), -1)
                cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 2)
                cv2.putText(img, str(id), (t_cx, t_cy), 0, 1, (0, 0, 255), 2)


        if box_len == 0 and len(now) > 0:
            vedio_tag = 1
            if len(labels) == 0:
                start_id = 0
            else:
                start_id = labels[len(labels) - 1]
            print("开始" + str(start_id))
            start_time = datetime.datetime.now()
            out = cv2.VideoWriter(
                './record_vedio/' + str(start_time.day) + str(start_time.hour) + str(start_time.minute) + str(
                    start_time.second) + '.avi', cv2.VideoWriter_fourcc(*'XVID'), 20,
                (640, 480))
        if box_len == 0 and len(now) == 0:  # 入侵结束
            if len(labels) > 0 and vedio_tag == 1:
                end_id = labels[len(labels) - 1]
                print("结束" + str(end_id))
                end_time = datetime.datetime.now()
                all_r = [start_time, end_id - start_id, end_time]
                # save(all_r)
                out.release()
                vedio_tag = 2
        img_origin[b1:b2, a1:a2] = img
        cv2.rectangle(img_origin, (a1, b1), (a2, b2), (0, 255, 0), 2)
        center_tracker = now.copy()
        # 传输上网页
        imgencode = cv2.imencode('.jpg', img_origin)[1]
        stringData = imgencode.tostring()
        yield (b'--frame\r\n'
               b'Content-Type: text/plain\r\n\r\n' + stringData + b'\r\n')
        if vedio_tag == 1:
            print("存入")
            out.write(cv2.resize(img_origin, (640, 480), interpolation=cv2.INTER_AREA))


    # thread.join()
# if __name__ == "__main__":
#     main()
