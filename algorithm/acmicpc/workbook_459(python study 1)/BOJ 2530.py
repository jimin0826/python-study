import sys

a, b, c = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
plus2 = (c + n) // 60
rem2 = (c + n) % 60
plus1 = (b + plus2) // 60
rem1 = (b + plus2) % 60

print((a + plus1) % 24, (b + plus2) % 60, rem2)