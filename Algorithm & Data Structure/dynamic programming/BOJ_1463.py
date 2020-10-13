import sys
X = int(sys.stdin.readline())
arr = [0 for i in range(X+1)]

for i in range(2, X+1):
    if(i % 3 == 0 and i % 2 == 0):
        arr[i] = min(arr[i//3], arr[i//2], arr[i-1]) + 1
    elif(i % 3 == 0):
        arr[i] = min(arr[i//3], arr[i-1]) + 1
    elif(i % 2 == 0):
        arr[i] = min(arr[i//2], arr[i-1]) + 1
    else:
        arr[i] = arr[i-1] + 1

print(arr[X])