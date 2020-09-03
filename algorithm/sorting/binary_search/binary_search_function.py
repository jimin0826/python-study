import sys

def binarySearch(arr, key):
  lowerbound = 0
  upperbound = len(arr) - 1
  while(True) :
    midPoint = (lowerbound + upperbound) // 2
    if(arr[midPoint] == key):
      return midPoint
    elif(arr[midPoint] < key ):
      lowerbound = midPoint + 1
    elif(arr[midPoint] > key):
      upperbound = midPoint - 1
    elif(arr[midPoint] != key):
      return -1
    

arr = [2, 9 ,10, 32, 5, 89, 5, 90, 76, 43, 28, 25, 
15, 71, 79, 82, 16, 49, 62, 86, 52, 28, 24, 25].sort()

print(binarySearch(arr, 53))