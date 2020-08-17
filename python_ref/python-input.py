import sys

# var1 = int(input())
# var2 = int(sys.stdin.readline())

# year_days = 366

# case 1 : one line one input(integer)
# num1 = int(sys.stdin.readline())
# print("input:", num1)

# case 2 : two line two inputs(integers)
# num2_1 = int(sys.stdin.readline())
# num2_2 = int(sys.stdin.readline())
# print("inputs:", num2_1, num2_2)

# case 3 : one line two inputs(integers)
# num3_1, num3_2 = map(int, sys.stdin.readline().split())
# print("inputs:", num3_1, num3_2)

# case 4 : one line two inputs using array
# numbers4 = list(map(int, sys.stdin.readline().split()))
# print("inputs:", numbers4)

# case 5 : three line three inputs
# num5_1 = int(sys.stdin.readline())
# num5_2 = int(sys.stdin.readline())
# num5_3 = int(sys.stdin.readline())
# print("inputs:", num5_1, num5_2, num5_3)

# case 6 : one line three inputs
# num6_1, num6_2, num6_3 = map(int, sys.stdin.readline().split())
# print("inputs:", num6_1, num6_2, num6_3)

# case 7 : one line three inputs using array
# numbers7 = list(map(int, sys.stdin.readline().split()))
# print("inputs:", numbers7)

# case 8 : one line N inputs using array
# numbers8 = list(map(int, sys.stdin.readline().split()))
# print("inputs:", numbers8)

# case 9 : N line N inputs using array(get N first)
# N = int(sys.stdin.readline())
# numbers9 = []

# for i in range(N) :
#     numbers9.append(int(sys.stdin.readline()))

# print('inputs:', numbers9)





# Practice 1
# 10줄에 걸쳐서 점수 10개를 입력받은 후, 점수의 평균을 구하는 프로그램을 작성하시오.
# N = 10 
# numbers = []

# for i in range(N) : 
#     numbers.append(int(sys.stdin.readline()))

# print(sum(numbers)/N)



# Practice 2
# 0이 입력될 떄까지 숫자를 계속 입력 받는다.(단, 줄은 계속 변한다.) 
# 0이 입력되기 전까지 입력된 숫자들의 합을 구하시오.

numbers = []

while(True) :
    num = int(sys.stdin.readline())
    if(num == 0 ):
        break
    else:
        numbers.append(num)
    
print(sum(numbers))


