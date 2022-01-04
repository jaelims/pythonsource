# pip install beautifulsoup4
# beautifulsoup : 파싱

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.v.daum.net/v/20220104102035295")
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

# 기자명
writer = soup.find("span", class_="txt_info")
print(writer.string)
