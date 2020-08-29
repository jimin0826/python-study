import sys

n = int(sys.stdin.readline())

if n % 4 == 0:
  if n % 400 == 0:
    print(1)
  elif n % 100 != 0:
    print(1)
  else:
    print(0)
else: 
  print
  