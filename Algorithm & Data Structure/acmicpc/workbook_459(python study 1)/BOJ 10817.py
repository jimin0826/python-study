import sys

numbers = list(map(int, sys.stdin.readline().split()))

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def bubbleSort(arr):
  for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
      if(arr[j] > arr[j+1]):
        swap(arr, j, j+1)
  return arr

newlist = bubbleSort(numbers)
print(newlist[len(newlist) - 2])