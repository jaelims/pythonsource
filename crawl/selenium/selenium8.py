# 새 창으로 뜨는 경우
from selenium import webdriver
import time

# 크롬 드라이버 로드
driver = webdriver.Chrome(
    "c:\\users\\user\\desktop\\source\\chromedriver\\chromedriver.exe"
)

driver.get("https://google.com")
print("현재 창 ", driver.title)
# 현재 창에 대한 정보 가져오기
parent_window = driver.current_window_handle

# 새 창 띄우기
driver.execute_script("window.open('https://www.naver.com')")

all_windows = driver.window_handles
child_window = [window for window in all_windows if window != parent_window][0]
driver.switch_to.window(child_window)
print("2. 현재 창 ", driver.title)
time.sleep(3)
driver.close()

# 부모 창으로 제어권 이동
driver.switch_to.window(parent_window)
time.sleep(1)
driver.close()
