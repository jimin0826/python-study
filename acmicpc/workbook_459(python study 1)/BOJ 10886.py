import sys

N = int(sys.stdin.readline())
cute = 0

for i in range(N):
  if int(sys.stdin.readline()) == 1:
    cute += 1

if cute > N//2:
  print('Junhee is cute!')
else:
  print('Junhee is not cute!')