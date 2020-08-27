import sys

M, N = map(int,sys.stdin.readline().split())

def isPrimeNumber(num):
  primeNum = True
  for d in range(2, num):
    if num % d == 0:
      primeNum = False
  return primeNum

for i in range(M, N+1):
  if isPrimeNumber(i) == True:
    print(i)  