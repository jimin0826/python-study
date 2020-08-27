import sys

def insertionSort(arr):
  n = len(arr)
  for i in range(1, n):
    temp = arr[i]
    for j in range(0, i):
      if(arr[j] > arr[i]):
        for k in range(i-1, j-1, -1):
          arr[k+1] = arr[k]
        arr[j] = temp
        break
  return arr

# To Do : inverse_insertionSort : sorted arr from the end of the list

def inverse_insertionSort(arr):
  n = len(arr)
  for i in range(n-1, -1, -1) :
    temp = arr[i] 
    ...

A = [6, 3, 2, 9, 10, 7, 1, 5]
A = insertionSort(A)
print(A)