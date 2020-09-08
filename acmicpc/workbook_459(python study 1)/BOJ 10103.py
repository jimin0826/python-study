import sys

n = int(sys.stdin.readline())
x = y = 100

for i in range(n):
  a, b = map(int, sys.stdin.readline().split())
  if a > b:
    y -= a
  elif a < b:
    x -= b

print(x)
print(y)
  