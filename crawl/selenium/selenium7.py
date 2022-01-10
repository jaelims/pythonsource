from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 크롬 드라이버 로드
driver = webdriver.Chrome(
    "c:\\users\\user\\desktop\\source\\chromedriver\\chromedriver.exe"
)

# 원하는 url로 접속
driver.get("http://python.org")

# 화면크기 제어
driver.maximize_window()

# element = driver.find_element(By.NAME, "q")
# element = driver.find_element(By.ID, "id-search-field")
# element = driver.find_element(By.CSS_SELECTOR, "#id-search-field")
# element = driver.find_element(By.CLASS_NAME, "search-field")
element = driver.find_element(By.TAG_NAME, "input")

element.send_keys("python")
element.send_keys(Keys.ENTER)

# 검색결과 페이지에서 타이틀 찾기
titles = driver.find_elements(By.TAG_NAME, "h3")

for title in titles:
    print(title.text)

# 소스 가져오기
# print(driver.page_source)


time.sleep(3)
# 드라이버 종료
driver.close()
