# set : 집합
# 중복을 허용하지 않음
# 순서가 없음

# s1 = set()
# s2 = set([1, 2, 3, 4, 5])
# s3 = set([1, 2, 3, 3, 5, 6])

# print(s1)
# print(s2)
# print(s3)

# # list => set
# list1 = [5, 6, 7, 8, 9]
# print(list1)
# print(set(list1))

# # set => list
# print(list(s2))

# # set => tuple
# print(tuple(s2))

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1.intersection(s2))
print(s1 & s2)

# 합집합
print(s1.union(s2))
print(s1 | s2)

# 차집합
print(s1.difference(s2))
print(s1 - s2)


# 추가
s1.add(7)
print(s1)

s1.add(4)
print(s1)

# 여러 개 추가 : update
s1.update([8, 9, 10])
print(s1)

# 제거 : remove
s1.remove(10)
print(s1)
