import math    
import numpy as np
import matplotlib.pyplot as plt
import math     

datas = [[0,1], [1, 2], [3, 1], [2, 4], [4, 6], [5, 3], [6, 3]]
B = [[0 for i in range(3)] for i in range(3)] 
Y = [0] * 3

for i in range(3) :
  for k in range(7) :
    Y[i] += datas[k][1]*math.pow(datas[k][0], i)
  for j in range(3) :
    result = 0
    for k in range(7) :
      B[i][j] += math.pow(datas[k][0], j)*math.pow(datas[k][0], i)

def transposeMatrix(m):
  T = [[0 for i in range(len(m))] for i in range(len(m))]
  for i in range(len(m)) : 
    for j in range(len(m)) : 
      T[i][j] = m[j][i]
  return T

def getMatrixMinor(m,i,j):
  return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
  #base case for 2x2 matrix
  if len(m) == 2:
    return m[0][0]*m[1][1]-m[0][1]*m[1][0]

  determinant = 0
  for c in range(len(m)):
    determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
  return determinant

def getMatrixInverse(m):
  determinant = getMatrixDeternminant(m)
  #special case for 2x2 matrix:
  if len(m) == 2:
    return [[m[1][1]/determinant, -1*m[0][1]/determinant],
            [-1*m[1][0]/determinant, m[0][0]/determinant]]

  #find matrix of cofactors
  cofactors = []
  for r in range(len(m)):
    cofactorRow = []
    for c in range(len(m)):
      minor = getMatrixMinor(m,r,c)
      cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
    cofactors.append(cofactorRow)
  cofactors = transposeMatrix(cofactors)
  for r in range(len(cofactors)):
    for c in range(len(cofactors)):
      cofactors[r][c] = cofactors[r][c]/determinant
  return cofactors

def product(m, vec) :
  n = len(vec)
  result = []
  for i in range(n) :
    value = 0
    for j in range(n) :
      value += m[i][j] * vec[j]
    result.append(value)

  return result   # Ax = b >> x = A-1b


print(B)
print(Y)
print(getMatrixDeternminant(B))
print(product(getMatrixInverse(B), Y))