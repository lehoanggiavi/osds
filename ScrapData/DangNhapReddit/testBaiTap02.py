from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd



# gecko_path = "E:/OSDS/osds/geckodriver.exe"
# # Khởi tởi đối tượng dịch vụ với đường geckodriver
# ser = Service(gecko_path)

# # Tạo tùy chọn
# options = webdriver.firefox.options.Options()
# options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
# # Thiết lập firefox chỉ hiện thị giao diện
# options.headless = False

# # Khởi tạo driver
# driver = webdriver.Firefox(options = options, service=ser)

# Dung trinh duyet Chrome
driver = webdriver.Chrome()


# Tạo url
url = 'https://nhathuoclongchau.com.vn/thuc-pham-chuc-nang/vitamin-khoang-chat'

# Truy cập
driver.get(url)

# Tạm dừng khoảng 2 giây
time.sleep(2)

# Tìm phần tử body của trang để gửi phím mũi tên xuống
body = driver.find_element(By.TAG_NAME, "body")
# print(driver.page_source)


# Lay them san pham
for _ in range(5):
    try:
        button_xemthem = driver.find_element(By.XPATH, "//div[@class='px-4 pt-3 md:px-0 md:pt-0']//span[contains(text(), 'Xem thêm')]")
        button_xemthem.click()
        time.sleep(3)
    except Exception as e:
        print(f"Loi {e}")


# Lazy loading
for i in range (40):
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.2)

# Tao ra cac ds de luu
stt=[]
ten_san_pham=[]
gia_ban=[]
hinh_anh=[]

# Tim tat ca the div
divs = driver.find_elements(By.XPATH, "//div[@class ='h-full relative flex rounded-xl border border-solid border-white bg-white transition-all duration-300 ease-out hover:border-blue-5 flex-col']")
for i, div in enumerate(divs, 1):
    
    try:
        tsp = div.find_element(By.XPATH, "./div[1]/div[1]//h3").text
        ten_san_pham.append(tsp)
    except Exception as e:
        print(f'Loi {e}')

    try:
        gsp = div.find_element(By.XPATH, "./div[1]//span").text
        gia_ban.append(gsp)
    except Exception as e:
        print(f'Loi {e}')
    
    try:
        ha = div.find_element(By.TAG_NAME, "img").get_attribute('src')
        hinh_anh.append(ha)
    except Exception as e:
        print(f'Loi {e}')

    if len(tsp)>0:
        stt.append(i)

# print(stt)
# print("################################")

# print(ten_san_pham)
# print("################################")

# print(gia_ban)
# print("################################")

# print(hinh_anh)
# print("################################")


# Tao ra 1 df
df = pd.DataFrame({
    "STT" : stt,
    "Ten San Pham" : ten_san_pham,
    "Gia Ban" : gia_ban,
    "Hinh Anh" : hinh_anh
})

print(df)

try:
    df.to_excel("Danh_sach_sp.xlsx", index=False)
except Exception as e:
    print(f"Loi {e}")