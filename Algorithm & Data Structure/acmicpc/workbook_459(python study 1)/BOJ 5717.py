import sys

a, b = map(int, sys.stdin.readline().split())

while not(a == 0 and b == 0):
  print(a + b)
  a, b = map(int, sys.stdin.readline().split())

