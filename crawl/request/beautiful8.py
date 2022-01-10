import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

headers = {"user-agent": UserAgent().chrome}

url = "https://finance.naver.com/"
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

# #container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr:nth-child(1) > th > a
pop_list = soup.select("div.aside_popular > table > tbody > tr")
for item in pop_list:
    # 종목명
    stock_name = item.find("a").string
    # 현재금액
    stock_price = item.find("td").string

    print(stock_name, stock_price)
