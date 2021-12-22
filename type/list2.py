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
