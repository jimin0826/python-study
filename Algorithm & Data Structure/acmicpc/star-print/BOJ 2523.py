import sys

a = int(sys.stdin.readline())

for i in range(a):
  print('*'*(i+1))
for i in range(a+1,2*a):
  print('*'*(2*a-i))