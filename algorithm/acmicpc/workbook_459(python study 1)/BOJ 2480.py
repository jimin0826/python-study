import sys

a, b, c = map(int, sys.stdin.readline().split())

if a == b == c:
  print(a*1000 + 10000)
elif a == b:
  print(a*100 + 1000)
elif c == b:
  print(c*100 + 1000)
elif a == c:
  print(a*100 + 1000)
else:
  print(100*max(a, b, c))
