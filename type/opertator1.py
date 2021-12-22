# 연산자

# 문자열과 숫자의 + 는 허용하지 않음
str1 = "123" # 자바(자바스크립트) "123"+1 => 1231
print(int(str1) + 1) # can only concatenate str (not "int") to str

s1, s2, s3 = "100", "100.123", 999.999
print(s1 + s2) # 연결
# print(s1 + s2 + s3) # can only concatenate str (not "float") to str

# 대입연산자 : +=, -=, *=, /=, //=, %=
money, c500, c100, c50, c10 = 0,0,0,0,0

money = 7777

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print('동전 교환')
print("500원 : %d개" % c500)
print("100원 : %d개" % c100)
print("50원 : %d개" % c50)
print("10원 : %d개" % c10)
print("나머지 돈 : %d원" % money)

# 관계연산자 : >, <, >=, <=, !=, ==
print()
print("--- 관계연산자 ---")
a, b = 10, 0
print("a == b", a==b)
print("a != b", a!=b)
print("a >= b", a>=b)
print("a <= b", a<=b)

# 논리연산자 : and, or, not (자바 &&, || 사용못함)
print()
print("--- 논리연산자 ---")
a, b, c = 100, 60, 15
print("and ", a > b and b > c)
print("or ", a > b or b > c)
print("not", not b < c)