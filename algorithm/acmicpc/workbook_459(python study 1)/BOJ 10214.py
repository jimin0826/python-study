import sys

N = int(sys.stdin.readline())

for i in range(N): #이부분을 왜 해야하는지 모르겠음!
  Y = K = 0
  for i in range(9):
    y, k = map(int, sys.stdin.readline().split())
    Y += y
    K += k
  
  if Y > K: 
    print('Yonsei')
  elif Y < K:
    print('Korea')
  else:
    print('Draw')