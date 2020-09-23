import sys

numbersList = []

for i in range(3):
  numbersList.append(list(map(int, sys.stdin.readline().split())))
  
rowAverageList = []
colAverageList = []
AverageList = []
for i in range(3):
  average_row = sum(numbersList[i]) / 2
  rowAverageList.append(average_row)

print('가로평균 :', end ='')
for e in rowAverageList:
  print(round(e), end = ' ')
print()

for j in range(2):
  average_col = 0
  for i in range(3):
    average_col += numbersList[i][j]
  average_col /= 3
  colAverageList.append(average_col)

print('세로평균:', end = '')
for e in colAverageList:
  print(round(e), end = ' ')
print()

sum = 0
for i in range(3):
  for j in range(2):
    sum += numbersList[i][j]
print(sum /6) 
    

