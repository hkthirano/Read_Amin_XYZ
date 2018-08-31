import re
import numpy as np
import pandas as pd


def f_extract_xzy(lines, conf):

    f_first = True  # １行目の確認

    for line in lines:
        if f_first:
            tmp_xyz = re.findall('\s*(\S+)\s+(\S+)\s+(\S+)', line[30:55])
            data_xyz = np.array(
                [[tmp_xyz[0][0], tmp_xyz[0][1], tmp_xyz[0][2]]])
            f_first = False

        else:
            # xyzの座標を取り出す
            tmp_xyz = re.findall('\s*(\S+)\s+(\S+)\s+(\S+)', line[30:55])

            # 配列にする
            add_xyz = np.array([[tmp_xyz[0][0], tmp_xyz[0][1], tmp_xyz[0][2]]])

            # 下に結合していく
            # data_xyz.shape[0] => 追加する最後の行の場所
            data_xyz = np.insert(data_xyz, data_xyz.shape[0], add_xyz, axis=0)

    return data_xyz


def f_extract_xzy_with_weight(lines, conf, weight_type):
    # 重みデータ読み込み
    df_weight = pd.read_csv('./Weight/sample.csv').set_index('Amin')

    f_first = True  # １行目の確認

    for line in lines:
        if f_first:
            tmp_xyz = re.findall('\s*(\S+)\s+(\S+)\s+(\S+)', line[30:55])
            amin = line[17:20]
            weight = df_weight.loc[amin, weight_type]
            data_xyz = np.array(
                [[tmp_xyz[0][0], tmp_xyz[0][1], tmp_xyz[0][2], weight]])
            f_first = False

        else:
            # xyzの座標を取り出す
            tmp_xyz = re.findall('\s*(\S+)\s+(\S+)\s+(\S+)', line[30:55])

            # 重みを読み取る
            amin = line[17:20]
            weight = df_weight.loc[amin, weight_type]

            # 配列にする
            add_xyz = np.array(
                [[tmp_xyz[0][0], tmp_xyz[0][1], tmp_xyz[0][2], weight]])

            # 下に結合していく
            # data_xyz.shape[0] => 追加する最後の行の場所
            data_xyz = np.insert(data_xyz, data_xyz.shape[0], add_xyz, axis=0)

    return data_xyz


def f_save_extract_xyz(data_xyz, save_file_path):
    f = open(save_file_path, 'w')
    np.savetxt(save_file_path, data_xyz.astype(np.float32), delimiter=' ')
    f.close()
