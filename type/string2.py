# 문자열 함수

# 1. count
# a = "hobby"
# print("a안에 포함된 b 문자 개수", a.count("b"))

# 2. find()
# a = "Python is best choice"
# print("b가 시작되는 위치", a.find("b"))
# print("b가 시작되는 위치", a.find("b", 12))

# print("k가 시작되는 위치", a.find("k"))

# # 3. index() : find와 다르게 없는 문자열이라면 Exception 발생
# print("b가 시작되는 위치", a.index("b"))
# print("k가 시작되는 위치", a.index("k"))  # ValueError: substring not found

# 4. startswish() / endswith() : 특정 문자열로 시작하고 끝나는지 확인
# a = "Python is best choice"
# print(a.startswith("P"))
# print(a.endswith("P"))

# 5. join()
# a = ","
# print("문자열 삽입", a.join("abcd"))
# print("a", "b", "c", "d", sep=",")

# 6. upper() / lower() / swapcase()
# a = "abcdef"
# print(a.upper())
# b = "ABCDEF"
# print(b.lower())
# c = "Python is Easy"
# print(c.swapcase())

# 7. strip() / lstrip() / rstrip() - 공백제거
# a = "     h1"
# print(a.strip(), a.lstrip())
# b = "     h1       "
# print(b.strip())
# print("    hi" == "hi")  # False

# 8. replace() - 문자열 변경
# a = "Life is too short"
# print(a.replace("Life", "Your leg"))

# 9. split() - 문자열 나누기
# a = "Life is too short"
# print(a.split())  # ['Life', 'is', 'too', 'short']
# b = "a:b:c:d"
# print(b.split(":"))  # ['a', 'b', 'c', 'd']
# c = "하나\n둘\n셋"
# print(c.split("\n"))  # ['하나', '둘', '셋']

# 10. 문자열 구성 파악 - 숫자로 구성되어 있는가?
# print("1234".isdigit())
# print("abcd".isalpha())
# print("abc123".isalnum())
# print("ABCD".isupper())
# print("   ".isspace())


# 문제

# 대문자는 소문자로, 소문자는 대문자로 출력
name = "KennRY"

print(name.swapcase())

# 년/월/일 형태로 입력받고 10년 후의 날짜를 구한 후 출력
# date = input("년/월/일 : ")
# pos = date.find("/")
# year = int(date[0:pos]) + 10
# month = date[5:7]
# day = date[8:]
# print("10년 후 날짜 : %d년 %s월 %s일" % (year, month, day))


# 사이트 별로 비밀번호를 만들어 주는 프로그램 작성
# 예) http://naver.com 이라면
# 규칙 1 : http:// 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
# 결과 : 생성된 비밀번호는 nav51!
site = input("사이트 주소 : ")
pw1 = site[site.find("/") + 2 : site.find(".")]
pw2 = pw1[:3] + str(len(pw1)) + str(pw1.count("e")) + "!"
print(pw2)
