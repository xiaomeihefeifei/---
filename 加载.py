#coding=gbk
import pandas as pd
import os
path = r'G:\������̫��������\1.����'

def get_file():                   #����һ�����б�
    files =os.listdir(path)
    files.sort() #����
    list= []
    for file in files:
        if not  os.path.isdir(path +file):  #�жϸ��ļ��Ƿ���һ���ļ���
            f_name = str(file)
#             print(f_name)
            tr = '\\'   #������һ��б��
            filename = path + tr + f_name
            list.append(filename)
    return list

list = get_file()
print('\\')
print(list[:6]

'''data = pd.read_csv(list[2])
print(data.head())'''