import sys

n = int(sys.stdin.readline())

for i in range(1,n):
    print(' ' * (n-i) + '*' * (2*i - 1))
for i in range(1, n+1):
    print(' '*(i-1) + '*' *((2*n + 1)-2*i))