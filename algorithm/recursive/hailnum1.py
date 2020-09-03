import sys

n = int(sys.stdin.readline())

def hailnum_length(n):
  print(n, end = " ")
  if(n == 1):
    return
  else:
    print("->", end = " ")
    if(n % 2 == 0):
      hailnum_length(n // 2)
    else:
      hailnum_length(3*n + 1)

hailnum_length(n)
