import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

num = str(A*B*C)

count_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(num)) :
    count_arr[int(num[i])] += 1

print(count_arr)

for i in range(10) : 
    print(count_arr[i])