# 변수 선언 : 어떤 데이터를 담을 것인지에 따라서 타입이 결정
a = 3
b = 4

print("a+b=", a+b)
print("a-b=", a-b)
print("a*b=", a*b)
print("a/b=", a/b) # 0.75
print("a//b=", a//b) # 0 (자바에서 사용했던 나누기 개념과 동일) 
print("a**b=", a**b)
print("a%b=", a%b)

# 타입변환 - bool(타입변환할 값 or 변수)
print()
print("99", type(99), bool(99), type(bool(99))) # True
print("99", type("99"), bool("99"), type(bool("99"))) # True
print("0", type("0"), bool("0"), type(bool("0"))) # True
print("0", type(0), bool(0), type(bool(0))) # False
print("1", type(1), bool(1), type(bool(1))) # True
print("0.1", type(0.1), bool(0.1), type(bool(0.1))) # True

# str()
print()
print(str(3), type(str(3)))
print(str(3.5), type(str(3.5)))
print(str(1.0e4), type(str(1.0e4)))
print(str(True), type(str(True))) # "True"
print(str(False), type(str(False)))

# int()
print()
print(int(False), type(int(False)))
print(int(True), type(int(True)))
print(int(98.6), type(int(98.6)))
print(int(1.0e4), type(int(1.0e4)))
print(int("1"), type(int("1")))
# print(int("1.0e4"), type(int("1.0e4"))) 소수점, 지수를 포함하는 문자열은 변경 안됨

# float()
print()
print(float(False), type(float(False)))
print(float(True), type(float(True)))
print(float(98), type(float(98)))
print(float("98.6"), type(float("98.6")))