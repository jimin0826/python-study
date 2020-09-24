import sys

n = int(sys.stdin.readline())

def hailnum(n):
  print(n, end = " ")
  if(n == 1):
    return
  else:
    print("->", end = " ")
    if(n % 2 == 0):
      hailnum(n // 2)
    else:
      hailnum(3*n + 1)

hailnum(n)
