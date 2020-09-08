import sys

n = int(sys.stdin.readline())

for i in range(n):
  a, b, c = map(int, sys.stdin.readline().split())
  if b > a + c:
    print('advertise')
  elif b == a + c:
    print('does not matter')
  else:
    print('do not advertise')