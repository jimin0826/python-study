N = int(input())

count = 0

for _ in range(N):
  ip = input()
  stack = []

  for c in ip:
    if len(stack)!= 0 and stack[-1] == c:
      stack.pop()
    
    else:
      stack.append(c)

  if stack == []:
    count += 1

print(count)