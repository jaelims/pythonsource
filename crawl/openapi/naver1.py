import requests

headers = {
    "X-Naver-Client-Id": "zu2TZE3Z7saqNKEdJtvJ",
    "X-Naver-Client-Secret": "s7oqBhZCE0",
}

res = requests.get(
    "https://openapi.naver.com/v1/search/shop.json?query=아이폰", headers=headers
)

# print(res.json())

data = res.json()

for item in data["items"]:
    print(item["title"], item["link"])
