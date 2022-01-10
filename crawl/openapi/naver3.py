import requests
from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active

# isbn
ws1.column_dimensions["A"].width = 30
# title
ws1.column_dimensions["B"].width = 100
# price
ws1.column_dimensions["C"].width = 15
# discount
ws1.column_dimensions["D"].width = 15

# 제목 행 삽입
ws1.append(["isbn", "title", "price", "discount"])
# 시트명 지정
ws1.title = "베르나르 베르베르"

headers = {
    "X-Naver-Client-Id": "zu2TZE3Z7saqNKEdJtvJ",
    "X-Naver-Client-Secret": "s7oqBhZCE0",
}

start = 1
for idx in range(10):
    start_num = start + (idx * 100)

    url = (
        "https://openapi.naver.com/v1/search/book.json?query=베르나르_베르베르&display=100&start="
        + str(start_num)
    )

    res = requests.get(url, headers=headers)

    data = res.json()

    for item in data["items"]:
        ws1.append([item["isbn"], item["title"], item["price"], item["discount"]])

wb.save("베르나르.xlsx")
wb.close()
