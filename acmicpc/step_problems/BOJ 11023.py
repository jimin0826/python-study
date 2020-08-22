import sys

T = list(map(int, sys.stdin.readline().split()))
sum = 0
for i in range(len(T)):
  sum += T[i]

print(sum)