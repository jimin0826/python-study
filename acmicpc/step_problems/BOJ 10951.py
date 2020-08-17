import sys

for i in sys.stdin:
    num1, num2 = map(int, i.split())
    print(num1+num2)