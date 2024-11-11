from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Khoi tao duong dan file chromedriver:
chrome_path = "E:/OSDS/osds/chromedriver.exe"


# Dieu khien file driver
ser = Service(chrome_path)

# Khoi tao trinh duyet
driver = webdriver.Chrome(service=ser)

# Khoi tao web

driver.get(url='http://books.toscrape.com')

time.sleep(3)

body_tags = driver.find_element(By.TAG_NAME, 'body')

for _ in range(50):
    body_tags.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.3)



