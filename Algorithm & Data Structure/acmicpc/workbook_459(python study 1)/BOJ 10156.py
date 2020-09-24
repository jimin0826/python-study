import sys

K, N, M = map(int, sys.stdin.readline().split())
answer = (K*N)-M 

if answer > 0:
    print(answer)
else:
    print(0)