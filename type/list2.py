# 리스트 연산자

# + : 리스트 더하기
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)
# print(a[0] + b[1])

# * : 반복
# a = [1, 2, 3]
# print(a * 3)

# 리스트 수정
# a = [1, 2, 3]
# a[2] = 4
# print(a)
# a[1] = "Life"
# print(a)

# b = [4, 5, 6]
# b[1:2] = [10, 11]  # [4, 10, 11, 6]
# b[1] = [10, 11]  # [4, [10, 11], 6]
# print(b)

# 리스트 삭제
a = [1, 2, 3]
# a[1:3] = []
# print(a)
# del a[1]
# print(a)  # [1, 3]
# del a # del 객체 ()

# 문제
# 리스트 안의 숫자가 100 이상인 숫자 출력하기
# numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# print("*" * 20)
# print("100 이상 숫자")
# print("*" * 20)
# for i in numbers:
#     if i >= 100:
#         print(i, end=" ")

# print()

# # 리스트 안의 숫자가 홀수인지 짝수인지 출력하기
# print("*" * 20)
# print("홀/짝 판별")
# print("*" * 20)
# for i in numbers:
#     if i % 2 == 0:
#         print(i, "= 짝수", end=", ")
#     else:
#         print(i, "= 홀수", end=", ")

# print()
# # 리스트 안의 숫자들의 자리수 출력하기
# print("*" * 20)
# print("각 숫자의 자릿수 출력")
# print("*" * 20)
# for i in numbers:
#     print("{} : {} 자릿수".format(i, len(str(i))), end=", ")

# print()

# 아래 리스트를 풀어서 출력
# list_of_list = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]

# 출력결과 1 2 3 4 5 6 7 8 9
# for list in list_of_list:
#     for i in list:
#         print(i, end=" ")


# 리스트 함수
# 1) append() : 마지막에 요소 추가
# list1 = [1, 2, 3]
# print(list1)

# 하나의 요소 추가
# list1.append(7)
# print(list1)  # [1, 2, 3, 7]

# 여러 개의 요소 추가
# list2 = [4, 5, 6]
# # print(list1 + list2)  # [1, 2, 3, 7, 4, 5, 6]
# list1.append(list2)
# print(list1)  # [1, 2, 3, [4, 5, 6]]

# 1 ~ 100 숫자 중에서 짝수만 들어있는 리스트 생성하고 출력하기
# list = []
# for num in range(1, 101):
#     if num % 2 == 0:
#         list.append(num)
# print(list)


# 2) sort() : 정렬
# list1 = [25, 75, 15, 9, 6, 3, 35]
# print("정렬 전", list1)
# list1.sort()
# print("정렬 후", list1)

# list2 = ["k", "z", "b", "a", "q", "r"]
# print("정렬 전", list2)
# list2.sort()
# print("정렬 후", list2)

# a 97, A 65
# list3 = ["k", "z", "B", "a", "Q", "r"]
# print("정렬 전", list3)
# list3.sort()
# print("정렬 후", list3)

# list4 = ["ㅎ", "ㅋ", "ㄱ", "ㄷ", "ㅈ", "ㄹ"]
# print("정렬 전", list4)
# list4.sort()
# print("정렬 후", list4)

# list5 = ["abc", "tail", "bcd", "test", "animal", "korea"]
# print("정렬 전", list5)
# list5.sort()
# print("정렬 후", list5)

# sort(reverse=True) : 내림차순 정렬
# list1 = [25, 75, 15, 9, 6, 3, 35]
# print("정렬 전", list1)
# list1.sort(reverse=True)
# print("정렬 후", list1)


# 3) reverse() : 리스트 역순으로 처리
# print("\n")
# print("reverse() 사용")
# list1 = [25, 75, 15, 9, 6, 3, 35]
# print("정렬 전", list1)
# list1.sort()
# list1.reverse()
# print("정렬 후 거꾸로 출력", list1)


# 4) index() : 위치반환
# list1 = [34, 25, 9, 75]
# print("9가 있는가?", list1.index(9))
# print("45가 있는가?", list1.index(45))  # ValueError: 45 is not in list


# 5) insert() : 리스트 내의 특정 위치에 요소 삽입
# list1 = [34, 25, 9, 75]
# list1.insert(1, 56)
# print(list1)


# 6) remove() : 리스트 요소 제거
# list1 = [34, 25, 9, 75, 9]
# list1.remove(25)
# print(list1)
# list1.remove(9)  # 중복된 경우 앞 요소 제거
# print(list1)


# 7) pop() : 리스트 요소 맨 마지막 요소 돌려주고 요소는 삭제
# list1 = [34, 25, 9, 75, 9]
# list1.pop()
# print(list1)

# pop(인덱스 값) : 해당 인덱스 요소 돌려주고 그 요소는 삭제
# print(list1.pop(1))
# print(list1)


# 8) count() : 리스트 내의 특정 요소의 개수 세기
# list1 = [34, 25, 9, 75, 9]
# print(list1.count(9))


# 9) extend() : 리스트 확장(+ 와 같은 결과)
# list1 = [34, 25, 9, 75, 9]
# list2 = [11, 12, 13]
# list1.extend(list2)
# print(list1)


# 10) clear() : 리스트 요소 모두 삭제
# list1.clear()
# print(list1)  # []

# 리스트 안의 요소가 비어 있는 경우는 false 인식
# list1 = [1]
# if list1:
#     print("True")
# else:
#     print("False")

# str1 = ""
# if str1:
#     print("True")
# else:
#     print("False")

# 요소 in 리스트 : 해당 요소가 리스트안에 들어있는지 판별
# fruit = ["사과", "배", "딸기", "수박", "메론"]

# if "딸기" in fruit:  # not in
#     print("딸기 있음")
# else:
#     print("딸기 없음")


# enumerate() : 인덱스 값 사용
# list1 = [23, 12, 36, 53, 19]

# for item in list1:
#     print(item)

# print()

# for item in enumerate(list1):
#     print(item)

# print()

# for idx, item in enumerate(list1, start=1):
#     print("%d : %d" % (idx, item))

# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70,60,55,75,95,90,80,85,100]
# A 학급의 평균을 구하시오
# list1 = [70, 60, 55, 75, 95, 90, 80, 85, 100]
# total = 0
# for jumsu in list1:
#     total += jumsu
# avg = total / len(list1)
# print("A 학급의 평균 %.2f" % avg)
# print("A 학급의 평균 %.2f" % (sum(list1) / len(list1)))


# ord() : 코드 값 반환
# print(ord("A"))  # 65

# chr() : 코드값을 문자로 반환
# print(chr(65))  # A


# 주차장 프로그램
# 총 5대의 차가 주차 가능 / 맨 마지막 차랑부터 빠져나갈 수 있음

# parking_lot = []
# top, car_name = 0, "A"

# while True:
#     no = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 : "))

#     if no <= 3:
#         if no == 1:
#             if top >= 5:
#                 print("주차장 꽉 찼음")
#             else:
#                 parking_lot.append(car_name)
#                 print("{} 자동차 들어감. 주차장 상태 ==> {}".format(car_name, parking_lot))

#                 top += 1
#                 car_name = chr(ord(car_name) + 1)
#         elif no == 2:
#             if top == 0:
#                 print("빠져나갈 자동차가 없음")
#             else:
#                 outCar = parking_lot.pop()
#                 print("{} 자동차 나감. 주차장 상태 ==> {}".format(outCar, parking_lot))

#                 top -= 1
#                 car_name = chr(ord(car_name) - 1)
#         else:
#             print("프로그램 종료")
#             break
#     else:
#         print("번호를 확인해 주세요")


# List Comprehension

# 1 ~ 100

# numbers = []
# for n in range(1, 101):
#     numbers.append(n)

# numbers = list(range(1, 101))
# print(numbers)

# numbers = [n for n in range(1, 101)]
# print(numbers)

# list1 = ["갑", "을", "병", "정", "경"]
# 정을 제외하고 출력
# for s in list1:
#     if s != "정":
#         print(s)

# list2 = [s for s in list1 if s != "정"]
# print(list2)

# 1~100까지 홀수를 리스트로 생성하고 출력
# list1 = [x for x in range(1, 101) if x % 2 == 1]
# print(list1)

# 아래 리스트 항목 중에서 5글자 이상의 단어만 출력
# list1 = ["nice", "study", "python", "anaconda", "java"]
# list2 = [x for x in list1 if len(x) >= 5]
# print(list2)

# 소문자만 모아서 새로운 리스트로 생성하고 출력
# list1 = ["A", "b", "c", "D", "E", "f", "G", "h"]
# list2 = [a for a in list1 if a.islower()]
# print(list2)

# 각 요소의 2배를 한 리스트를 생성하고 출력
# list1 = [1, 2, 3, 4, 5]
# list2 = [x * 2 for x in list1]
# print(list2)

# print([x * x for x in range(5)])

print([[x, x + 1, x + 2] for x in [1, 2, 3]])
