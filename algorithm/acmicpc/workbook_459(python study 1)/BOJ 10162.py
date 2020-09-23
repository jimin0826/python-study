import sys

N = int(sys.stdin.readline())

a = N//300
b = (N-a*300)//60
c = (N-a*300-b*60)//10
if (N%10 == 0):
  print(a, b, c)
else:
  print(-1)
  