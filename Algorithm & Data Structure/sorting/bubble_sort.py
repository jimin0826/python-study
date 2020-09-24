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

def inverse_bubbleSort(arr):
  for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
      if(arr[len(arr)-j-1] < arr[len(arr)-j-2]):
        swap(arr, len(arr)-j-1, len(arr)-j-2)
    #print(i, j, arr)
  return arr

myarr = [6, 3, 2, 9, 10, 7, 1, 5]
myarr = inverse_bubbleSort(myarr)
print(myarr)