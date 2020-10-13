
def STAIR_NUMBER():
    N = int(input())
    if(N==1):
        print(9)
        return

    stair_num = [[0 for i in range(10)] for j in range(N)]
    for i in range(10):
        stair_num[0][i] = 1
                          
    for i in range(1, N):
        stair_num[i][0] = stair_num[i-1][1]
        stair_num[i][9] = stair_num[i-1][8]
        for j in range(1, 9):
            stair_num[i][j] = stair_num[i-1][j-1] + stair_num[i-1][j+1]

    print(sum(stair_num[N-1][1:])%1000000000)

STAIR_NUMBER()
    