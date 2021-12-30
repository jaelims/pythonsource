# 파일 입력
# r(읽기), w(쓰기), a(덧붙이기)
# rb(읽기+binary), wb(쓰기+binary) => 이미지, 실행파일...

# read() : 전체 읽어오기
# f = open("./test1.txt", "r", encoding="utf-8")
# print(f.read())
# f.close()

# with open("./test1.txt", "r", encoding="utf-8") as f:
#     print(f.read())

# readline() : 줄 단위로 읽어오기
# f = open("./test2.txt", "r", encoding="utf-8")
# print(f.readline()) 한 줄만 읽어옴
# line = f.readline()
# while line:
#     print(line, end="")
#     line = f.readline()

# with open("./test2.txt", "r", encoding="utf-8") as f:
#     line = f.readline()
#     while line:
#         print(line, end="")
#         line = f.readline()

# readlines() : 파일의 내용을 리스트로 가져옴
# f = open("./test2.txt", "r", encoding="utf-8")
# print(f.readlines())

# with open("./test2.txt", "r", encoding="utf-8") as f:
#     for name in f:
#         # print(name) 엔터가 자동으로 들어감
#         print(name.strip())

# score.txt 파일을 읽어와서 합계와 평균 출력
# list() 처리 : sum() 함수 사용 가능, len() 함수 사용 가능
# score = []
# with open("./score.txt", "r", encoding="utf-8") as f:
#     for num in f:
#         score.append(int(num))
#     print(score)

# print("점수 총합 : {}".format(sum(score)))
# print("점수 평균 : {}".format(sum(score) / len(score)))


# info.txt 읽어서 BMI 지수를 계산한 후 화면에 출력
# bmi = 몸무게 / (키 / 100) ** 2
# bmi가 25이상이면 과체중, 18.5 이상이면 정상체중, 나머지는 저체중
# 출력결과
# 차다 43 182

# user = []
# with open("./info.txt", "r", encoding="utf-8") as f:
#     for info in f:
#         name, weight, height = info.strip().split(", ")

#         print(name, weight, height)

#         bmi = int(weight) / (int(height) / 100) ** 2

#         result = ""
#         if 25 <= bmi:
#             result = "과체중"
#         elif 18.5 <= bmi:
#             result = "정상체중"
#         else:
#             result = "저체중"

#         # 이름 : 차다
#         print("이름 : {}".format(name))
#         # 몸무게 : 43
#         print("몸무게 : {}".format(weight))
#         # 키 : 182
#         print("키 : {}".format(height))
#         # bmi : 12.9234
#         print("bmi : {}".format(bmi))
#         # 결과 : 저체중
#         print("결과 : {}".format(result))
#         print()


# 원본 파일을 읽어서 암호화 시킨 후 저장
# 암호화된 파일을 읽어서 원래대로 출력

content = ""

while True:
    no = int(input("1. 암호화 | 2. 복호화 | 3. 종료 >> "))

    if no == 1:
        # 원본 파일 읽어오기
        with open("./origin.txt", "r", encoding="utf-8") as f:
            content = f.read()
        # 암호화 시킨 후 새 파일로 저장
        # ord() : 해당 문자의 유니코드 값 리턴 / chr() : 유니코드값을 문자로 리턴
        with open("./encryption.txt", "w", encoding="utf-8") as f:
            for c in content:
                f.write(chr(ord(c) + 100))  # chr(ord(a) + 100)
    elif no == 2:
        with open("./encryption.txt", "r", encoding="utf-8") as f:
            content = f.read()
            for a in range(0, len(content)):
                print(chr(ord(content[a]) - 100), end="")
            print()
    else:
        break
