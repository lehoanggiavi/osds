from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"Lay tat ca duong link va ten cua nhom hoac nhac si choi cho the loai am nhac do"

"Khoi tao web"
driver = webdriver.Chrome()

"Mo trang web"
url = "https://en.wikipedia.org/wiki/List_of_acid_rock_artists"

driver.get(url)
time.sleep(5)

"Tim tat ca the ul"
tags_ul = driver.find_elements(By.TAG_NAME, "ul")

"Tim the ul tuong ung"
# for index, value in enumerate(tags_ul):
#     print(f"Index: {index}, Value: {value.text}")

"Lay tat ca the li trong the ul[24]"
tags_li = tags_ul[24].find_elements(By.TAG_NAME, "li")

"Trong the li lay the a "
"Vi the a co chua Atribute href va title"
links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href")for tag in tags_li]
titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title")for tag in tags_li]

for link in links:
    driver.get(link)
time.sleep(3)
driver.quit()

    # print(link)

# for title in titles:
#     print(title)
