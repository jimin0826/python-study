import sys

numList = list(map(int, sys.stdin.readline().split()))

count_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(numList)):
    count_array[numList[i]] += 1    

for i in range(1,11):
    print("{}의 개수 : {}".format(i, count_array[i]))

