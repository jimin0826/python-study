import sys

def T(a,b):
  if b % a == 0:
    return 'factor'
  elif a % b == 0:
    return 'multiple'
  else:
    return 'neither'

while(True):
  a, b = map(int, sys.stdin.readline().split())
  if(a == 0 and b == 0) :
    break
  print(T(a,b))
