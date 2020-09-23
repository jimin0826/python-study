import sys

numList = []
for i in range(9):
    numList.append(int(sys.stdin.readline()))

max_num = numList[0]
max_num_index = 0
for i in range(9):
    if(max_num < numList[i]) :
        max_num = numList[i]
        max_num_index = i

print(max_num)
print(max_num_index + 1)
