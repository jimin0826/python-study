import sys

n = int(sys.stdin.readline())

def hailnum_length_length(n):
  if(n == 1):
    return 1
  else:
    if(n % 2 == 0):
      1 + hailnum_length(n // 2)
    else:
      hailnum_length(3*n + 1)

hailnum_length(n)
