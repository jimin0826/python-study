import sys

numList = []

for i in range(7) :
  num = int(sys.stdin.readline())
  if(num % 2 == 1) :
    numList.append(num)
  else :
    pass

if len(numList) == 0:
  print(-1)
else:
  print(sum(numList))
  print(min(numList))
