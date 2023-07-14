# 导入包

from aip import AipSpeech
from imutils import paths
from playsound import playsound

from managementcenter.views.faceCollection.facial import FaceUtil
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import os
import shutil
import time

# 控制参数
error = 0
start_time = None
limit_time = 2  # 2 秒
counter = 0
faceutil = FaceUtil()

action_list = ['blink', 'open_mouth', 'smile', 'rise_head', 'bow_head', 'look_left', 'look_right']
action_map = {'blink': '请眨眼', 'open_mouth': '请张嘴',
              'smile': '请笑一笑', 'rise_head': '请抬头',
              'bow_head': '请低头', 'look_left': '请看左边',
              'look_right': '请看右边'}
imagedir = 'managementcenter/views/faceCollection/faceInfo/images'
# global variable
dataset_path = 'managementcenter/views/faceCollection/faceInfo/images'
output_encoding_file_path = 'managementcenter/views/models/face_recognition_hog.pickle'
image_paths = list(paths.list_images(dataset_path))
output_file = 'managementcenter/views/faceCollection/voices/output.mp3'

# 在百度AI平台创建应用获取以下信息
APP_ID = '36160094'
API_KEY = 'gRSHCGOWWDtVKeGrA3n3NIwU'
SECRET_KEY = 'xNvD1kaEuOpRxsxSGi817vGoTFzGQbF0'


def text_to_speech(text, output_file):
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result = client.synthesis(text, 'zh', 1, {
        'vol': 5,
        'spd': 5,
        'pit': 5,
        'per': 3
    })

    if not isinstance(result, dict):
        with open(output_file, 'wb') as f:
            f.write(result)


def collectingfaces(image, id, counter):
    global error, start_time, limit_time
    image = cv2.flip(image, 1)

    if error == 1:
        end_time = time.time()
        difference = end_time - start_time
        print(difference)
        if difference >= limit_time:
            error = 0

    face_location_list = faceutil.get_face_location(image)
    for (left, top, right, bottom) in face_location_list:
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

        face_count = len(face_location_list)
        if error == 0 and face_count == 0:  # 没有检测到人脸
            print('[WARNING] 没有检测到人脸')
            # audioplayer.play_audio(os.path.join(audio_dir, 'no_face_detected.mp3'))
            error = 1
            start_time = time.time()
        elif error == 0 and face_count == 1:  # 可以开始采集图像了
            print('[INFO] 可以开始采集图像了')
            # audioplayer.play_audio(os.path.join(audio_dir, 'start_image_capturing.mp3'))
            break
        elif error == 0 and face_count > 1:  # 检测到多张人脸
            print('[WARNING] 检测到多张人脸')
            # audioplayer.play_audio(os.path.join(audio_dir, 'multi_faces_detected.mp3'))
            error = 1
            start_time = time.time()
        else:
            pass
    # 新建目录
    if counter == 0 and error != 1:
        print(imagedir + '/' + str(id))
        print(os.path.exists(imagedir + '/' + str(id)))
        if os.path.exists(imagedir + '/' + str(id)):
            shutil.rmtree(imagedir + '/' + str(id), True)
        os.mkdir(imagedir + '/' + str(id))
        print('[Tips] 目录创建成功')
        counter += 1
    if counter <= 4 and error != 1:
        img_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_PIL)
        draw.text((int(image.shape[1] / 2), 30), "准备开始采集", font=ImageFont.truetype(r'../msyh.ttc', 40),
                  fill=(255, 0, 0))  # 显示字
        # 转换回OpenCV格式
        image = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
        counter += 1
    if 4 < counter < 109 and error != 1:
        action_name = action_map[action_list[(counter - 4) // 15]]
        if ((counter - 4) % 15) == 1:
            text_to_speech(action_name, output_file)
            playsound(output_file)
        print('%s-%d' % (action_name, counter - 4))
        print((counter - 4) // 15)
        origin_img = image.copy()  # 保存时使用

        img_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_PIL)
        draw.text((int(image.shape[1] / 2), 30), action_name, font=ImageFont.truetype(r'../msyh.ttc', 40),
                  fill=(255, 0, 0))  # 显示字

        # 转换回OpenCV格式
        image = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)

        image_name = os.path.join(imagedir, str(id),
                                  action_list[(counter - 4) // 15] + '_' + str((counter - 4)) + '.jpg')
        cv2.imwrite(image_name, origin_img)  # 保存
        counter += 1
    if 109 <= counter < 113 and error != 1:
        img_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_PIL)
        draw.text((int(image.shape[1] / 2), 30), "采集结束", font=ImageFont.truetype(r'../msyh.ttc', 40),
                  fill=(255, 0, 0))  # 显示字
        if counter == 109:
            text_to_speech("采集结束", output_file)
            playsound(output_file)
        # 转换回OpenCV格式
        image = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
        counter += 1
    if 113 <= counter < 117 and error != 1:
        img_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_PIL)
        draw.text((int(image.shape[1] / 2), 30), "等待训练中", font=ImageFont.truetype(r'../msyh.ttc', 40),
                  fill=(255, 0, 0))  # 显示字
        if counter == 113:
            text_to_speech("等待训练中", output_file)
            playsound(output_file)
        # 转换回OpenCV格式
        image = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
        counter += 1
    if counter == 117 and error != 1:
        faceutil.save_embeddings(image_paths, output_encoding_file_path)
        counter += 1
    if counter > 117 and error != 1:
        img_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_PIL)
        draw.text((int(image.shape[1] / 2), 30), "训练完成", font=ImageFont.truetype(r'../msyh.ttc', 40),
                  fill=(255, 0, 0))  # 显示字
        if counter == 118:
            text_to_speech("训练完成", output_file)
            playsound(output_file)
        # 转换回OpenCV格式
        image = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
        counter += 1
    return image, counter
