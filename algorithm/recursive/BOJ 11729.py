import sys

n = int(sys.stdin.readline())
paths = []
def hanoi(n, start, through, destination) :
  if(n == 1) :
    paths.append([start, destination])
  else :
    hanoi(n-1, start, destination, through) 
    hanoi(1, start, through, destination)
    hanoi(n-1, through, start, destination)
  
hanoi(n, 1, 2, 3)
print(len(paths))

for path in paths:
  print(*path)