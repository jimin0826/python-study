fibo_arr = [1, 2, 3, 5, 8, 13, 21, 34]

def fibo(n):
  if(len(fibo_arr) > n):
    return fibo_arr[n-1]
  else:
    while(len(fibo_arr) != n):
      fibo_arr.append(fibo_arr[-1] + fibo_arr[-2])
    return fibo_arr[n-1]

n = int(input())
print(fibo(n) % 10007)