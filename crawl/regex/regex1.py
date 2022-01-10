# 정규표현식 - 자바스크립트와 동일

import re

# /정규식/,
# compile() : 정규식을 저장해주는 메소드

pattern = re.compile("D.A")  # . : 모든 문자랑 매치


# 정규식과 매치 확인 - search(), sub(), match()
result = pattern.search("DAA")
print(result)
