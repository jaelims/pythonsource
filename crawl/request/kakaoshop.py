# 베스트100 두개의 카테고리 지정 후 1~100위까지 출력
import requests

url = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest"

params = [
    {"vCateId": "B02", "durationDays": 30, "count": 100, "_": 1641261658885},
    {"vCateId": "E01", "durationDays": 30, "count": 100, "_": 1641262497212},
]


with requests.Session() as s:
    for param in params:
        r = s.get(url, params=param)

        for i, item in enumerate(r.json(), 0):
            print(i + 1, item["product_name"])
        print()
