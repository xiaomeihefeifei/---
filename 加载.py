#coding=gbk
import pandas as pd
import os
path = r'G:\李鹏飞太赫兹数据\1.苗期'

def get_file():                   #创建一个空列表
    files =os.listdir(path)
    files.sort() #排序
    list= []
    for file in files:
        if not  os.path.isdir(path +file):  #判断该文件是否是一个文件夹
            f_name = str(file)
#             print(f_name)
            tr = '\\'   #多增加一个斜杠
            filename = path + tr + f_name
            list.append(filename)
    return list

list = get_file()
print('\\')
print(list[:6]

'''data = pd.read_csv(list[2])
print(data.head())'''