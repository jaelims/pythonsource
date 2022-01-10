from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome(
    "c:\\users\\user\\desktop\\source\\chromedriver\\chromedriver"
)

driver.get("https://www.naver.com")

element = driver.find_element_by_name("query")

element.send_keys("안드로이드")
element.send_keys(Keys.RETURN)

print(driver.page_source)

time.sleep(3)
driver.close()
