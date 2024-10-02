from selenium import webdriver
from selenium.webdriver.common.by import By
import time
"Khởi tạo web"
driver = webdriver.Chrome()

"Mở 1 trang web"
driver.get("https://gomotungkinh.com")
time.sleep(2)

# Tìm phần tử img có id là "bonk"
bonk_img = driver.find_element(By.ID, "bonk")
while True:
    bonk_img.click()
    print("Click on bonk image")
    time.sleep(0.5)


