word = input()
n = len(word)
result = 1
if n % 2 == 0:
  for i in range(0, n // 2):
    if word[i] == word[n-i-1]:
      pass
    else:
      result = 0
elif n % 2 == 1:
  for i in range(0, (n-1) //2):
    if word[i] == word[n -1 -i]:
      pass
    else:
      result = 0

print(result)