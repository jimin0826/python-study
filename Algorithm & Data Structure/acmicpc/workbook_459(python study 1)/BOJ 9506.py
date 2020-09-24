import sys

while True: 
  N = int(sys.stdin.readline())
  if N == -1: 
    break

  listA = []
  number = 0
  for i in range(1, N):
    if N % i == 0:
      listA.append(i)
  for i in range(len(listA)):
    number += listA[i]


  if N == number:
    print(f'{N} = {" + ".join(map(str, listA))}')
  else: 
    print(f'{N} is NOT perfect.')