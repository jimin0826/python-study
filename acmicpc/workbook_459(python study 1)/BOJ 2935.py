import sys

a = int(sys.stdin.readline())
b = sys.stdin.readline().strip()
c = int(sys.stdin.readline())

if b == '*':
  print(a * c)
else:
  print(a + c)

  #sys을 쓰려면 strip을 써야함.