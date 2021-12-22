# 문자열 자료형
# '', "", """ """, ''' '''
str1 = "Hello World"
str2 = "Hello World"

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
str3 = "Life is too short\nYou need Python"

# str3 = """Hello World"""  # ''' '''
str4 = """
    Hello World
    Life is too short
    You need Python
"""

str5 = "Hello's"

# print(str4)

# # 문자열 응용
# # + : 결합
# print("Python" + " is fun")

# # * : 복제
# print("Python" * 2)

# print("*" * 50)
# print("My Program")
# print("*" * 50)

# 문자열 인덱싱과 슬라이싱
# 0부터 시작, 뒤에서 인덱싱 -1
str1 = "Life is too short"
# print(str1[3])  # 인덱싱 e
# print(str1[-1])  # t
# print(str1[-5])  # s

# print(str1[0:4])  # Life
# print(str1[4:8])  #  is
# print(str1[9:])  # oo short
# print(str1[:17])  # Life is too short
# print(str1[0:-4])  # Life is too s

str2 = "20190701Sunny"
# 문자열을 두 부분으로 나누어 출력하기(날짜, 날씨)
# date = str2[:8]
# weather = str2[8:]
# print(date, ", ", weather)

# # 날짜를 2019-07-01 출력하기
# year = date[:4]
# month = date[4:6]
# day = date[6:]
# print(year, month, day, sep="-")

# # 주민등록번호에서 성별 확인하기
# # 남자 : 1,3    여자 : 2,4
# str1 = "901205-3234567"
# if str1[7] == "1" or str1[7] == "3":
#     print("남자")
# elif str1[7] == "2" or str1[7] == "4":
#     print("여자")

str1 = "대한민국"
for s in str1:
    print(s)


# 문자열 길이
print("문자열 길이 : ", len(str1))
