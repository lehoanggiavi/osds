# import pandas as pd
# data = {'name': ["Le Hoang Gia Vi", "Nguyen Thi My Chi",  "Le Hoang Kieu Vy", "Le Minh Phung", "Le Thi Thao"],
#         'age': [20, 20, 16, 41, 39]
#
#         }
# row_lables = [1, 2, 3, 4, 5]
#
# df = pd.DataFrame(data=data)
# print(df)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# "Khoi tao web"
# driver = webdriver.Chrome()
#
# url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22P%22"
# driver.get(url)
# time.sleep(2)
# print(url)
#
# tags_a = driver.find_elements(By.TAG_NAME, "a")
#
# links = [tag.get_attribute("href") for tag in tags_a]
# print(links)
#
# for link in links:
#     print(link)



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

"Lấy tất cả các tên của họa sĩ theo bảng chữ cái"

"Khoi tao Web"
driver = webdriver.Chrome()

"Mo trang"
url = "https://en.wikipedia.org/wiki/Lists_of_painters"
driver.get(url)
"""
    Thêm mới 
        Dòng dưới có tác dụng đợi các thành phần của web tải động
"""
WebDriverWait


"""Lay tat ca cac the <a> voi title chua 
'List_of_painters'"""
# tags_a = driver.find_elements(By.XPATH, "//a[contains(@title, 'List of painters by name')]")
tags_a = driver.find_elements(By.TAG_NAME, 'a')
print(tags_a)


"Tao ra danh sach lien ket"
links = [tag.get_attribute("href") for tag in tags_a]

"Xuat thong tin"
# count = 0
for link in links:
#     if count > 1:
#         break
    print(link)

# "Dong webdriver"
# driver.quit()

