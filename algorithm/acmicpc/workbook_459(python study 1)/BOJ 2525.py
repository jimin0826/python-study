import sys

a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
plus = (b + c) // 60
rem = (b + c) % 60

print((a + plus) % 24, b + rem)

