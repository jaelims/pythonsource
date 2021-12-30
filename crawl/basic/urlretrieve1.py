# urlretrieve
# 요청하는 url의 정보를 로컬 파일로 저장
# csv 파일, api 데이터 등 많은 양의 데이터를 한번에 저장할 때 사용

import urllib.request as req

url = "http://google.com"

save_url = "c:\\users\\user\\Desktop\\google.html"

try:
    file1, header1 = req.urlretrieve(url, save_url)
except Exception as e:
    print(e)
else:
    print("성공")
    print(header1)
