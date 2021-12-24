# return : 결과값은 언제나 하나

# def sum_and_mul(a, b):
#     return a + b, a * b

# sum, mul = sum_and_mul(3, 4)
# print(sum, mul)


# def func_mul(x):
#     y1 = x * 100
#     y2 = x * 200
#     y3 = x * 300

#     # return y1, y2, y3 # 결과값은 튜플로 리턴(기본)
#     return [y1, y2, y3]  # 결과값은 리스트로 리턴


# result = func_mul(100)
# print(result)

# result1, result2, result3 = func_mul(200)
# print(result1, result2, result3)


# def say_nick(nick):
#     if nick == "바보":
#         return
#     print("나의 별명은 %s 입니다." % nick)


# say_nick("바보")
# say_nick("야호")


# 사칙연산 함수
# 3 + 4 = 7, 두 개의 숫자와 하나의 연산자를 받아서 사칙연산(+, -, *, //)

# def four_rules(num1, num2, op):
#     if op == "+":
#         return num1 + num2
#     elif op == "-":
#         return num1 - num2
#     elif op == "*":
#         return num1 * num2
#     elif op == "//":
#         return num1 // num2

# a, b = 6, 3
# print("{} {} {} = {}".format(a, "+", b, four_rules(a, b, "+")))
# print("{} {} {} = {}".format(a, "-", b, four_rules(a, b, "-")))
# print("{} {} {} = {}".format(a, "*", b, four_rules(a, b, "*")))
# print("{} {} {} = {}".format(a, "/", b, four_rules(a, b, "//")))

# a = int(input("첫번째 숫자 : "))
# b = int(input("두번째 숫자 : "))
# op = input("연산자 입력 : ")
# print("{} {} {} = {}".format(a, op, b, four_rules(a, b, op)))


# 1~100 수 중에서 소수를 구하는 함수
# 소수 : 1과 자기 자신으로만 나누어지는 1보다 큰 양의 정수
# 2,3,5,7,11...

# prime_list = []


# def isPrime(x):
#     cnt = 0
#     for i in range(1, x + 1):
#         if x % i == 0:
#             cnt += 1
#     if cnt == 2:
#         prime_list.append(x)


# for j in range(1, 101):
#     isPrime(j)

# print(prime_list)  # 소수가 담긴 리스트 출력


# 중첩된 리스트를 하나의 리스트로 반환
output = []


def flatten(data):
    for item in data:
        if type(item) == list:
            flatten(item)  # 재귀호출
        else:
            output.append(item)
    return output


example = [[1, 2, 3], [4, 5, 6], 7, [8, 9]]
print("원본", example)
print("변환", flatten(example))
