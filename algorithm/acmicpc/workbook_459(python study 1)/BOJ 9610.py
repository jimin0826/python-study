import sys

n = int(sys.stdin.readline())

num1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0

for i in range(n):
  a, b = map(int, sys.stdin.readline().split())

  if (a == 0 or b == 0):
    AXIS += 1
  elif(a > 0 and b > 0):
    num1 += 1
  elif(a > 0 and b < 0):
    Q4 += 1
  elif(a < 0 and b < 0):
    Q3 += 1
  else:
    Q2 += 1

print("Q1: {}".format(num1), 
"Q2: {}".format(Q2),
"Q3: {}".format(Q3),
"Q4: {}".format(Q4), 
"AXIS: {}".format(AXIS), sep='\n')