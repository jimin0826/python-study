# Independent Alleles

def factorial(n):
  result = 1
  for i in range(1, n+1):
    result *= i
  return result

def combination(i, j):
  return factorial(i) / (factorial(j) * factorial(i - j))

def independent_alleles(k, n):
  p = 0
  count = pow(2, k)      
  for i in range(n, count+1):
    p += combination(count, i) * pow(0.25, i) * pow(0.75, count - i)
  return p

with open("input.txt", "r") as f:
  k, n = [int(i) for i in f.readline().strip().split()]
print(independent_alleles(k,n))