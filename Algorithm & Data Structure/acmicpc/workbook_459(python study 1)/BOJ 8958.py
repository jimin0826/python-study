n = int(input())

for i in range(n):
  ox = input()
  score = 0
  T = 0
  for j in range(len(ox)):
    if ox[j] == 'O':
      T += 1
      score += T
    elif ox[j] == 'X':
      score += 0
      T = 0
  print(score)