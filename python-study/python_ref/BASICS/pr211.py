import sys

def gcd(n,m) :
  result = min(n, m)
  while(True) :
    left_m = m % result
    left_n = n % result
    if(left_m == 0 and left_n == 0) :
      break
    else :
      result -= 1
  return result


def lcm(n, m) :
  result = max(n, m)
  while(True) :
    left_m = result % m
    left_n = result % n
    if(left_m == 0 and left_n == 0) : 
      break
    else :
      result += 1
  return result

print(gcd(20, 120))
print(lcm(4,6))


