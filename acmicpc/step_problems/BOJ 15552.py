import sys

case = int(input())

for i in range(case):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(num1 + num2)