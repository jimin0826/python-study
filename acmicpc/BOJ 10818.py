import sys

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))

max_num = numList[0]
min_num = numList[0]
for i in range(1,N):
    if(max_num < numList[i]):
        max_num = numList[i]
    if(min_num > numList[i]):
        min_num = numList[i]

print(min_num, max_num)
print(help(.append()))