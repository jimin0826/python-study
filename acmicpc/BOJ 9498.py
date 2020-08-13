import sys

n = int(sys.stdin.readline())

if(n > 100 or n < 0) :
    print("ScoreOutofRangeError")
elif(n >= 90) :
    print('A')
elif(n >= 80) :
    print('B')
elif(n >= 70):
    print('C')
elif(n >= 60):
    print('D')
else :
    print('F')
    