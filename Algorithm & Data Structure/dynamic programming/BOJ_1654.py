import sys
k, n = map(int, sys.stdin.readline().split())
list = []
for _ in range(k):
  list.append(int(sys.stdin.readline()))

low, high = 1, max(list)

while low <= high:
  mid = (low + high) // 2
  print(mid, end = ':')
  sum_lines = 0

  for i in list:
    sum_lines += (i // mid) 
    print(sum_lines, end = '->')

  if sum_lines >= n:
    low = mid + 1
  else:
    high = mid - 1
  print(" ==> ({}, {})".format(low , high))

print(high)