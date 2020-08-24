import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
  print('*'*i, ' '*(2*N-2*i), '*'*i, sep='')
for i in range(1, N+1):
  print('*'*(N-i), ' '*2*i, '*'*(N-i), sep='')
  
