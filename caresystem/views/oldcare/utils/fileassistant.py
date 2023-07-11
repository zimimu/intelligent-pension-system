# -*- coding: utf-8 -*-
'''
文件处理相关的函数
'''


import pandas as pd


def get_people_info(people_info_path):
    dataset = pd.read_csv(people_info_path)

    # 得到ID->姓名的map
    id_card_to_name = {}
    id_card_to_type = {}

    for index, row in dataset.iterrows():
        id_card_to_name[row[0]] = row[1]
        id_card_to_type[row[0]] = row[2]

    return id_card_to_name, id_card_to_type


def get_facial_expression_info(facial_expression_info_path):
    dataset = pd.read_csv(facial_expression_info_path)

    # 得到摄像头ID->摄像头名字的map
    facial_expression_id_to_name = {}

    for index, row in dataset.iterrows():
        facial_expression_id_to_name[row[0]] = row[1]

    return facial_expression_id_to_name
