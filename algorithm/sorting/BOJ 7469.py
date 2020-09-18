import sys

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def bubbleSort(arr):
  for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
      if(arr[j] > arr[j+1]):
        swap(arr, j, j+1)
      #print(i, j, arr)
  return arr

a, b = map(int, sys.stdin.readline().split())
mylist = list(map(int, sys.stdin.readline().split()))

for i in range(b):
  p, q, r = map(int, sys.stdin.readline().split())
  extracted_list = mylist[p-1 : q]
  bub_extractedlist = bubbleSort(extracted_list)
  print(bub_extractedlist[r-1])

#되긴 하는데 시간초과.