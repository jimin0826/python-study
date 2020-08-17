import sys

def getDiceGameReward(l, m, n) :
  money = 0
  if(l == m and m == n) :
    money = 10000 + l * 1000
  elif(l == m) :
    money = 1000 + 100 * l
  elif(m == n) :
    money = 1000 + 100 * m
  elif(n == l) :
    money = 1000 + 100 * n
  else :
    money = 100 * max(l, m, n)
  return money

N = int(sys.stdin.readline())
money_list = []

for _ in range(N) :
  a, b, c = map(int, sys.stdin.readline().split())
  money_list.append(getDiceGameReward(a, b, c))

print(max(money_list))
