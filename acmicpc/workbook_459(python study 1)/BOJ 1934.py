import sys
T = int(sys.stdin.readline())

def gcd(a, b):
  gcd = 1
  for i in range(2, min(a,b) + 1):
    while (a % i == 0) and (b % i == 0):
      a = a // i
      b = b // i
      gcd = gcd * i 
      continue
  return gcd

def lcm(a, b):
  return a * b // gcd(a, b)

for i in range(T):
  a, b = map(int, sys.stdin.readline().split())
  print(lcm(a, b))