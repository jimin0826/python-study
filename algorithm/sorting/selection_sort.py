def swap(arr, i, j) :
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def selectionSort(arr) :
  for i in range(len(arr) - 1) :
    min_num = arr[i]  # initialization of minimum number
    min_index = i     # initialization of index of the minimum number
    for j in range(i+1, len(arr)) :
      if(arr[j] < min_num) :
        min_num = arr[j]
        min_index = j
    if(i != min_index) :
      swap(arr, i, min_index)
    print(i, arr)
  return arr

myarr = [6, 3, 2, 9, 10, 7, 1, 5]
myarr = selectionSort(myarr)
print(myarr)