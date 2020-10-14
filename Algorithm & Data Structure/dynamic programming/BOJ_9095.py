import sys

T = int(input())
numbers = []
for _ in range(T):
  numbers.append(int(sys.stdin.readline()))

minimum_representation_case = [1, 2, 4]

def minimum_case(n):
  if(len(minimum_representation_case) >= n):
    return minimum_representation_case[n-1]
  else:
    while(len(minimum_representation_case) != n):
      minimum_representation_case.append(
        sum(minimum_representation_case[-3:])
      )
    return minimum_representation_case[n-1]

for e in numbers:
  print(minimum_case(e))