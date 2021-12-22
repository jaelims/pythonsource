import datetime

now = datetime.datetime.now()
print(now) # 2021-12-21 10:18:06.520901
print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))

# 오전, 오후
if now.hour <= 12:
    print("{}년 {}월 {}일 오전 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
else:
    print("{}년 {}월 {}일 오후 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour-12, now.minute, now.second))

# 삼항 연산자
# 조건 ? 참 : 거짓(X)
# 참일때 실행하는 구문 if 조건 else 거짓일때

str = "안녕하세요" if True else "반갑습니다."
print(str)

# [] : 리스트, 비어 있는 경우 false
a = []
str = a if a else "비어있는 배열"
print(str)

# 중첩 if
a = 75
if a > 50:
    if a < 100:
        print("50보다 크고 100보다 작다")
    else:
        print("100보다 크다")
else:
    print("50보다 작다")

# 다중 조건
# if ~ elif ~ else

num = 90
if num >= 90:
    print("등급 A")
elif num >= 80:
    print("등급 B")
elif num >= 70:
    print("등급 C")
else:
    print("등급 D")

# 점수 구간에 맞춰 학점 출력하기
# 점수입력 받은 후 학점 출력
# A : 81 ~ 100
# B : 61 ~ 80
# C : 41 ~ 60
# D : 21 ~ 40
# E : 나머지

jumsu = int(input("점수 입력 : "))
if jumsu > 80:
    print("학점 : A")
elif jumsu > 60:
    print("학점 : B")
elif jumsu > 40:
    print("학점 : C")
elif jumsu > 20:
    print("학점 : D")
else:
    print("학점 : E")

# 산술 계산기 => 두 개의 숫자 입력 받기
# +, -, *, /, //, **, %

num1 = int(input("첫번째 수 입력 : "))
op = input("+, -, *, /, //, **, % 중 입력 : ")
num2 = int(input("두번째 수 입력 : "))

if op == "+":
    print(num1, op, num2, "=", num1+num2)
elif op == "-":
    print(num1, op, num2, "=", num1-num2)
elif op == "*":
    print(num1, op, num2, "=", num1*num2)
elif op == "/":
    print(num1, op, num2, "=", num1/num2)
elif op == "//":
    print(num1, op, num2, "=", num1//num2)
elif op == "**":
    print(num1, op, num2, "=", num1**num2)
elif op == "%":
    print(num1, op, num2, "=", num1%num2)