#conding=utf8
import os
import pandas as pd

a_list=[r"G:\李鹏飞太赫兹数据\1.苗期\1.0",r"G:\李鹏飞太赫兹数据\1.苗期\2.N20",r"G:\李鹏飞太赫兹数据\1.苗期\3.N60",
      r"G:\李鹏飞太赫兹数据\1.苗期\4.100",r"G:\李鹏飞太赫兹数据\1.苗期\5.N150",r"G:\李鹏飞太赫兹数据\1.苗期\6.P20",
      r"G:\李鹏飞太赫兹数据\1.苗期\7.P60",r"G:\李鹏飞太赫兹数据\1.苗期\8.P150",r"G:\李鹏飞太赫兹数据\1.苗期\9.K20",
      r"G:\李鹏飞太赫兹数据\1.苗期\10.K60",r"G:\李鹏飞太赫兹数据\1.苗期\11.K150"]
for a in a_list:
    print(a)
    g = os.walk(a)
    list = []
    for path, dir_list, file_list in g:
        for dir_name in file_list:
            filename = os.path.join(path, dir_name)
            list.append(filename)
    # list=list[2:]
    # print(filename)
    # print(list[1:3])
    c_list=['PW','RF','TR']
    for c in c_list:
        # b = [li for li in list if li.endswith(c+'.csv')]
        # b = [li for li in list if li.endswith('RF.csv')]
        b = [li for li in list if li.endswith(c + '.csv')]
        print(b)
        result = pd.DataFrame()
        # b=b[1:3]
        # print(b)
        for b1 in b:
            data = pd.read_csv(b1)
            result = pd.concat([result, data], axis=1)
            # result=result.append(data)
        # print(result)
        # result.to_csv('4.成熟期-K150-PW.csv')
        # result.to_csv('4.成熟期-K150-RF.csv')
        #result.to_csv('4.成熟期-K150-TR.csv')
        result.to_csv(a+c+'.csv')




