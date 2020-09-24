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
  for i in range(n-2, -1, -1) :
    print(i, end = '')
    temp = arr[i] 
    for j in range(i+1, n):
      if(arr[j] > arr[i]):
        for k in range(i+1, j):
          arr[k-1] = arr[k]
        arr[j-1] = temp
        break
      elif(j == n-1):
        for k in range(i+1, n):
          arr[k-1] = arr[k]
        arr[n-1] = temp
    print(arr)
  return arr

A = [6, 3, 2, 9, 10, 7, 1, 5]
A = inverse_insertionSort(A)
print(A)