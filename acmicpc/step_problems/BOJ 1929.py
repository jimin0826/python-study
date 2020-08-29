import sys

M, N = map(int,sys.stdin.readline().split())
primeNumbers = []

def isPrimeNumber(num):
  primeNum = True
  for d in primeNumbers:
    if num % d == 0:
      primeNum = False
      break
  return primeNum

for i in range(2, N+1):
  if isPrimeNumber(i) == True:
    print(i)  
    primeNumbers.append(i)