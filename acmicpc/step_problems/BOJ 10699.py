import sys

a = int(sys.stdin.readline())

for i in range(a):
  num, str = sys.stdin.readline().split()
  num = int(num)
  for i in range(len(str)):
    print(num*str[i],end='')
  print()