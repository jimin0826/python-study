import sys

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())

if(num1 > 0 and num2 > 0):
    print(1)
elif(num1 > 0 and num2 < 0):
    print(4)
elif(num1 < 0 and num2 < 0):
    print(3)
elif(num1 < 0 and num2 > 0):
    print(2)
