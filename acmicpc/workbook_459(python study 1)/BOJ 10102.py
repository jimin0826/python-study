N = int(input())
numList = list(str(input()))

A = B = 0
for i in numList:
  if i == 'A':
    A += 1
  else:
    B += 1

if A > B:
  print('A')
elif A == B:
  print('Tie')
else:
  print('B')