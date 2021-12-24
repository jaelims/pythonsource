# dictionary == map 개념 동일
# key, value
# {key1:value1, key2:value2}
# key 중복 시킬 수 없음

# 생성
dict1 = {"name": "Park", "age": 12}
print(dict1)

dict2 = {0: "Hello Python", 1: "Hello coding"}
print(dict2)

dict3 = {0: "Hello Python", 1: "Hello coding", 3: [1, 2, 3, 4, 5]}
print(dict3)

# 특정 키만 출력
# print(dict1["name"])
# print(dict2[0])
# print(dict3[3])
# print(dict1["addr"])


# 추가
# dict1["birth"] = "1223"
# print(dict1)

# dict2[2] = ["jsp", "java", "python"]
# print(dict2)


# numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
# counter = {}
# 출력 {1:3, 2:4, 6:1...}


# 삭제
# del dict1["age"]
# print(dict1)


# 함수

# 1) keys() : key 리스트 만들기
# print(dict1.keys())  # dict_keys(['name', 'age'])
# print(dict2.keys())
# print(dict3.keys())

# for k in dict1.keys():
#     print(k)


# 2) values() : value 리스트로 만들기
# print(dict1.values())
# print(dict2.values())
# print(dict3.values())

# for v in dict1.values():
#     print(v)


# 3) items() : key, value 쌍 가져오기
# print(dict1.items())
# print(dict2.items())
# print(dict3.items())

# for k, v in dict1.items():
#     print(k, v)


# 4) get() : key로 value 값 가져오기
# print(dict1.get("name"))
# print(dict1["name"])

# print(dict1.get("birth"))  # None
# print(dict1["birth"])  # KeyError: 'birth'


# 5) in : 해당 key가 딕셔너리 안에 있는지 확인
# print("name" in dict1)  # True
# print("birth" in dict1)  # False


dict4 = {"봄": "딸기", "여름": "수박", "가을": "사과", "겨울": "귤"}

# 계절만 출력
# for k in dict4.keys():
#     print(k, end=" ")

# 과일만 출력
# for v in dict4.values():
#     print(v, end=" ")

# 가을에 해당하는 과일 출력
print(dict4.get("가을"))
print(dict4["가을"])

# 딕셔너리에 사과가 포함되었는지 출력
for v in dict4.values():
    if v == "사과":
        print("있음")
        break
else:
    print("없음")

# 딕셔너리 컴프리헨션
# fruits = [fruit for fruit in dict4.values()]
# print(fruits)

# fruits = {fruit for fruit in dict4.values()}
# print(fruits)


# 딕셔너리를 생성하고 출력하기

# "A":90, "B":80, "C":70 의 값을 딕셔너리로 생성
dict5 = {"A": 90, "B": 80, "C": 70}
print(dict5)
# 위에 생성된 딕셔너리에 B키에 해당하는 값 출력
print(dict5["B"])
# B키 값을 삭제한 후 딕셔너리 출력
del dict5["B"]
print(dict5)

# "성인":10000, "청소년":7000, "아동":3000 딕셔너리 생성
dict6 = {"성인": 10000, "청소년": 7000, "아동": 3000}
print(dict6)
# "소아":0 항목 추가
dict6["소아"] = 0
print(dict6)
# key 값만 출력
print(dict6.keys())
# value 값만 출력
print(dict6.values())
