import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
answer = arr[0]
temp = [arr[0]]

for i in range(1,N):
  temp.append(max(arr[i], temp[i-1]+arr[i]))
  answer = max(answer, temp[i])

print(answer)