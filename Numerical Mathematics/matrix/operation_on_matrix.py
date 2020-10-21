import numpy as np
import matplotlib.pyplot as plt
import math     

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


def case_moments1(points) :
    ### Sorting points by x value 
    for i in range(len(points)-1) :
        for j in range(i+1, len(points)) :
            if(points[j][0] < points[i][0]) :
                temp = points[i]
                points[i] = points[j]
                points[j] = temp
    
    ### Initialize h, lambda, mu, d
    n = len(points)-1
    h = [0];     lmbd = [0];    mu = [0];      d = [0]
    for i in range(1, n+1) :
        h.append(points[i][0] - points[i-1][0])
    
    for j in range(1, n) :
        lmbd.append(h[j] / (h[j] + h[j+1]))
        mu.append(h[j+1] / (h[j] + h[j+1]))
        d.append(6 / (h[j] + h[j+1]) * ((points[j+1][1] - points[j][1]) / h[j+1] - (points[j][1] - points[j-1][1]) / h[j]))
    
    ### Construct Matrix
    if(n == 2) : return [0, d[1] / 2, 0]

    matrix = [[0 for i in range(n-1)] for j in range(n-1)]
    d_vec = [d[1]]
    matrix[0][0] = 2
    matrix[0][1] = mu[1]
    matrix[n-2][n-3] = lmbd[n-1]; matrix[n-2][n-2] = 2
    for i in range(1, n-2) :
        matrix[i][i-1] = lmbd[i+1]
        matrix[i][i] = 2
        matrix[i][i+1] = mu[i+1]
        d_vec.append(d[i+1])
    d_vec.append(d[n-1])

    inv_matrix = getMatrixInverse(matrix)  
    M_init = product(inv_matrix, d_vec)
    M = [0]
    for e in M_init :
        M.append(e)
    M.append(0)
    return M

