from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"Khoi tao web"
driver = webdriver.Chrome()

"Mo trang web"
url = "https://en.wikipedia.org/wiki/Lists_of_musicians"
driver.get(url)
time.sleep(2)

"""Trích xuất các liên kết đến trang web chứa thông tin về các nhạc sĩ chuyên về thể loại âm 
nhạc bắt đầu bằng chữ "A". In ra toàn bộ các đường link có liên quan đến các nhạc sĩ (bắt 
đầu bằng chữ List of)."""

"Tim tat ca the ul"
tags_ul = driver.find_elements(By.TAG_NAME, "ul")

"Tim the ul muon lay cac the loai nhac bat dau bang chu A"
# for index, value in enumerate(tags_ul):
#     print(f"Index: {index}, Value: {value.text}")

"Lay tat ca cac the li trong thr ul[21]"
tags_li = tags_ul[21].find_elements(By.TAG_NAME, "li")

links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href")for tag in tags_li]
for link in links:
    print(link)
    