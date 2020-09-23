# string

# str(number) : number(수)를 string(문자열)로 변환
print(str(12345)) # 12345
num = 98765
print(str(num)) # 98765
print(str(num)[2]) # 7

# len(my_str) : my_str(string)의 길이 전달
my_str = "apple"
print(len(my_str)) # 5




# general

# range(n) : <0, 1, 2, ..., n-1>
for i in range(5) :
    print(i, end = ', ')