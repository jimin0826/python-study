import sys
T = int(input())

def gcm(a, b):
  gcd = 1
  for i in range(2, min(a,b) + 1):
    while (a % i == 0) and (b % i == 0):
      a = a // i
      b = b // i
      gcd = gcd * k 
      continue
  return gcd

def lcm(a, b):
  return a * b // gcd(a, b)

for i in range(T):
  a, b = map(int, input().split())
  print(lcm(a, b))