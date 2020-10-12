# Rabbits and Recurrence Relations

import sys

def rabbitFiboNumber(n, k):
  if(n in {0, 1, 2}):
    return 1
  else: 
    return rabbitFiboNumber(n-1, k) + k * rabbitFiboNumber(n-2, k)


def main():
  n, k = map(int, sys.stdin.readline().split())
  print(rabbitFiboNumber(n, k))

main()