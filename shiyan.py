#conding=utf8
import os
import pandas as pd

g = os.walk(r"G:\李鹏飞太赫兹数据\4.成熟期\11.K150")
list=[]
for path,dir_list,file_list in g:
    for dir_name in file_list:
        filename=os.path.join(path, dir_name)
        list.append(filename)
#list=list[2:]
        #print(filename)
#print(list[1:3])
#b = [li for li in list if li.endswith('PW.csv')]
#b = [li for li in list if li.endswith('RF.csv')]
b = [li for li in list if li.endswith('TR.csv')]
#print(b)
result=pd.DataFrame()
#b=b[1:3]
#print(b)
for b1 in b:
    data=pd.read_csv(b1)
    result=pd.concat([result, data], axis=1)
    #result=result.append(data)
#print(result)
#result.to_csv('4.成熟期-K150-PW.csv')
#result.to_csv('4.成熟期-K150-RF.csv')
result.to_csv('4.成熟期-K150-TR.csv')

