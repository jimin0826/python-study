import sys

N, K = map(int, sys.stdin.readline().split())
numbersN = list(map(int, sys.stdin.readline().split()))

numbersN.sort()

print(numbersN[K-1])

