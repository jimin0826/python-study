import sys

N = int(sys.stdin.readline())
listA = []
number = 0

for i in range(1, N+1):
  if N % i == 0:
    listA.append(i)
print(listA)
for i in range(len(listA)):
  number += listA(i)

print(number)