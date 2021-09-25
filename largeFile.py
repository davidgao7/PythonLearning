import pandas as pd
import numpy as np

file_name = input("需要扫描的文件名：")
extension = file_name.split('.')[1]

file = None

if extension == 'txt':
    file = pd.read_csv(file_name, sep=' ', names = ['row'])
elif extension == 'csv':
    file = pd.read_csv(file_name, sep=',', names = ['row'])

n = int(input('输入你想把文件分为几份'))
groups = np.array_split(file, n)
for group in groups:
    print(group)
    print(type(group))

i = 0
writer = pd.ExcelWriter('result.xlsx')
for group in groups:
    group.to_excel(writer, sheet_name="Sheet"+str(i+1))
    i+=1
writer.save()
