from math import gcd
import sys

a, b = map(int, sys.stdin.readline().split())

gcd = gcd(a, b)
lcm = a * b // gcd

print(gcd)
print(lcm)