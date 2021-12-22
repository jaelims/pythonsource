# 리스트 자료형
# 배열, list 같은 개념
# 인덱스로 접근, 삽입, 삭제 가능
# 인덱스 값들은 특정 타입을 제한하지 않음

# 리스트 생성
# list1 = []
# list2 = [1, 2, 3]
# print(list1)
# print(list2)

# list1 = list()
# list2 = list([1, 2, 3])
# print(list1)
# print(list2)

# list3 = ["a", "b", "c", 1, 2]
# print(list3)

# list4 = ["a", "b", "c", 1, 2, 6.5, True]
# print(list4)

# list5 = ["a", "b", "c", ["Life", "is", "short"]]
# print(list5)

# 인덱싱과 슬라이싱
# list3 = ["a", "b", "c", 1, 2]
# print("list3[0]", list3[0])
# print("list3[-1]", list3[-1])

# list5 = ["a", "b", "c", ["Life", "is", "short"]]
# print("list5[2]", list5[2])
# print("list5[3]", list5[3])
# print("list5[3][0]", list5[3][0])
# print("list5[3][-1]", list5[3][-1])

# list6 = ["1", "2", ["a", "b", ["Life", "is", "short"]]]
# print("list6[2][2][1]", list6[2][2][1])
# print("list6[-1][-1][-2]", list6[-1][-1][-2])


list3 = ["a", "b", "c", 1, 2]
print("list3[0:3]", list3[0:3])
print("list3[:3]", list3[:3])
print("list3[:-2]", list3[:-2])

list5 = ["a", "b", "c", ["Life", "is", "short"]]
print("list5[3:]", list5[3:])  # [['Life', 'is', 'short']]
print("list5[3][:2]", list5[3][:2])  # ['Life', 'is']
