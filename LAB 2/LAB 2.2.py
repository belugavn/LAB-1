import numpy as np 
import pandas as pd 
df = pd.read_csv('E:/diem_hoc_phan.csv')
diem = df[['HP 1','HP 2','HP 3']].values.tolist()
diem1 =np.array(diem)
print(diem1)

def quydoi(diem):
   if 8.5<=diem<=10:
      return 'A+'
   elif 8<=diem<=8.4:
      return 'A'
   elif 7.5<=diem<=7.9:
      return 'B+'
   elif 7<=diem<=7.4:
      return 'B'
   elif 6.5<=diem<=6.9:
      return 'B+'
   elif 6<=diem<=6.4:
      return 'C'
   elif 5.5<=diem<=5.9:
      return 'C+'
   elif 5<=diem<=5.4:
      return 'D'
   elif diem<=5:
    return 'F'
xephang = []
for row in diem1:
 xephang1 = []
 for diem1 in row:
   xephang1 = xephang.append(quydoi(diem))
 xephang.append(xephang1)
xephang = np.array(xephang1)