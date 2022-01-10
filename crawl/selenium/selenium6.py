# selenium + BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

import time

# 크롬 드라이버 로드
driver = webdriver.Chrome(
    "c:\\users\\user\\desktop\\source\\chromedriver\\chromedriver.exe"
)

# 원하는 url로 접속
driver.get("http://python.org")

# 화면크기 제어
driver.maximize_window()

element = driver.find_element(By.NAME, "q")

element.send_keys("python")
element.send_keys(Keys.RETURN)

# 검색결과 페이지에서 타이틀 찾기 - BeautifulSoup 이용
res = BeautifulSoup(driver.page_source, "html.parser")

titles = res.find_all("h3")
print("titles", titles)

for title in titles:
    print(title.text)

# 소스 가져오기
# print(driver.page_source)


time.sleep(3)
# 드라이버 종료
driver.close()
