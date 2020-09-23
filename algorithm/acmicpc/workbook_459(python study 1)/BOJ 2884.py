import sys

a, b = map(int, sys.stdin.readline().split())

c = a*60 + b

if (a != 0):
  num = ((c - 45) // 60) % 24
  print(num, (b+15) % 60)
elif (a == 0 and b < 45):
  print(23, (b+15))
else:
  print(0, b-45)