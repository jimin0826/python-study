N = int(input())

result = [[" " for _ in range(N)] for _ in range(N)]

def makestar(N, x, y) :
  if(N == 3) :
    for i in range(3) :
      for j in range(3) :
        if(i == 1 and j == 1):
          pass
        else:
          result[x+i][y+j] = "*"
  else :
    n = N // 3
    for i in range(3):
      for j in range(3):
        if(i == 1 and j == 1):
          makeblank(n, x + i*n, y + j*n)
        else:
          makestar(n, x + i*n, y + j*n)

def makeblank(N, x, y):
  if(N == 3) :
    for i in range(3) :
      for j in range(3) :
        result[x+i][y+j] = " "
  else :
    for i in range(N):
      for j in range(N):
        result[x+i][y+j] = " "

makestar(N, 0, 0)

for i in range(N):
  for j in range(N):
    print(result[i][j], end = '')
  print()