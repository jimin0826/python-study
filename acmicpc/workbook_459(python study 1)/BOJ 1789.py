import sys

n = int(sys.stdin.readline())
num = 0

while num*(num +1) // 2 <= n:
  num += 1

print(num -1)