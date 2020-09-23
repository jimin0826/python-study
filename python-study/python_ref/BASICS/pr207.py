import sys

def swap(i, j, arr):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

my_arr = [5, 1, 7, 2, 6, 3]
print(my_arr) # before swap

i,j = 3, 5
swap(i, j, my_arr)
print(my_arr) # after swap
