from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd



"Tao noi chu dataframe rong"
d = pd.DataFrame({"Name": []})
# , "YearActive": []})

"Khoi tao web"
driver = webdriver.Chrome()

"Mo trang web"
url = "https://en.wikipedia.org/wiki/List_of_acid_rock_artists"
driver.get(url)
time.sleep(3)

"lay tat ca the ul"
ul_tags = driver.find_elements(By.TAG_NAME, "ul")

"Lay tat ca the li co trong ul tuong ung"
li_tags = ul_tags[24].find_elements(By.TAG_NAME, "li")

"Lay tat ca the a co thuoc tinh 'title'"
titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title")for tag in li_tags]
links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href")for tag in li_tags]

for title in titles:
    print(title)

for link in links:
    print(link)




