import sys

a, b = map(int,sys.stdin.readline().split())
c = list(map(int,sys.stdin.readline().split()))

for i in range(a):
  if b > c[i] :
    print(c[i], end = ' ')
