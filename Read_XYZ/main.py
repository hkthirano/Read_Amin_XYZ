# -*- coding: utf-8 -*-
# python3

import sys
import os

pwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(pwd + '/fRead')

# print(sys.path)

from F_f_m_l import *  # 関数 f_matching_line, f_save_matching_lines
from F_e_xyz import *  # 関数 f_extract_xzy(), f_save_extract_xyz


class Read_xyz():
    def __init__(self, file_path, conf):
        self.file_path = file_path
        self.f = open(self.file_path)
        #print("File read success!")
        self.conf = conf

    # ①:configの条件にマッチする行を取り出す
    def matching_lines(self):
        self.lines = f_matching_lines(self.f, self.conf)

    # ①のデータを保存する
    def save_matching_lines(self, save_file_path):
        f_save_matching_lines(self.lines, save_file_path)

    # ②-1:①のデータから座標を取り出す
    def extract_xyz(self):
        self.data_xyz = f_extract_xzy(self.lines, self.conf)

    # ②-2:①のデータから座標を取り出す & 重み付け
    def extract_xyz_with_weight(self, weight_type):
        self.data_xyz = f_extract_xzy_with_weight(
            self.lines, self.conf, weight_type)

    # ②-1.2のデータを保存する
    def save_extract_xyz(self, save_file_path):
        f_save_extract_xyz(self.data_xyz, save_file_path)
