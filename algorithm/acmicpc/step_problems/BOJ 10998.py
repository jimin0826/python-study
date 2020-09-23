import sys

# Case 1 : 하나의 문자열 입력받기
# str1 = sys.stdin.readline()
# print("Input :", str1)

# Case 2 : 하나의 정수 입력받기
# num2 = int(sys.stdin.readline())
# print("Input :", num2)

# Case 3 : 두 개의 정수 입력받기(두 줄에 입력받기)
# num3_1 = int(sys.stdin.readline())
# num3_2 = int(sys.stdin.readline())
# print("Two numbers :", num3_1, num3_2)

# Case 4 : 세 개의 정수 입력받기(세 줄에 입력받기)
# num4_1 = int(sys.stdin.readline())
# num4_2 = int(sys.stdin.readline())
# num4_3 = int(sys.stdin.readline())
# print("Three numbers :", num4_1, num4_2, num4_3)

# Case 5 : 두 개의 정수 입력받기(한 줄에 입력받기) input : 34 19
#num5_1, num5_2 = map(int, sys.stdin.readline().split())
#print(num5_1, num5_2)

# Case 6: 열 개의 정수 입력받기(리스트를 활용)
numbers6 = list(map(int, sys.stdin.readline().split()))
print(sum(numbers6))
