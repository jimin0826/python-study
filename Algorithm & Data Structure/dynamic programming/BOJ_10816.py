#10816
import sys
_ = input()
N = sorted(map(int,sys.stdin.readline().split()))
_ = input()
M = map(int,sys.stdin.readline().split())

def binary(N, n):
   low = 0
   high = len(N) - 1

   while low <= high:
      mid = (low + high) // 2
      if n == N[mid]:
         return N[low :high+1].count(n)
      elif n < N[mid]:
         high = mid - 1
      else:
         low = mid + 1
   return False 

n_dic = {}
for n in N:
    if n not in n_dic:
      n_dic[n] = binary(N,n)

for x in M:
  if x in n_dic:
    print(str(n_dic[x]), end = ' ')
  else:
    print('0', end = ' ')

