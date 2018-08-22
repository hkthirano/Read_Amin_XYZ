import re


def f_matching_lines(f, conf):

    chain = conf[0]

    if conf[1] == 'NA':
        f_flag = False  # フラグメントが存在するというフラグ
        flag_s = False
        flag_e = False
    else:
        f_flag = True
        flag_s = int(conf[1])
        flag_e = int(conf[2])

    data_list = []
    line = f.readline()
    while line:
        # 最初のモデルのみ読み込む
        if re.search('ENDMDL', line[0:6]):
            break

        # ATOMでCAでChainのところを探す
        if (re.search('ATOM', line[0:4])) and (re.search('CA', line[13:15])) and (re.search(chain, line[21:22])):
            atom_num = re.findall('\s*(\S+)', line[22:26])

            # フラグメント番号の範囲
            if f_flag and (flag_s <= int(atom_num[0]) <= flag_e):
                data_list.append(line)
            # フラグメントがない場合
            elif f_flag == False:
                data_list.append(line)

        line = f.readline()

    return data_list


def f_save_matching_lines(lines, save_file_path):
    f = open(save_file_path, 'w')
    for x in lines:
        f.write(str(x))
    f.close()
