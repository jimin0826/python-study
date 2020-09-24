import sys

def to_bin(n):
  if(n == 0):
    return "0"
  if(n == 1):
    return "1"
  else:
    return to_bin(n // 2) + str(n % 2)

def to_tern(n):
  for i in range(3):
    if(i == n) :
      return str(n)
  return to_tern(n // 3) + str(n % 3)

print(to_tern(5))
