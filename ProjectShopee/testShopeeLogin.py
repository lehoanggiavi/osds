import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Khởi tạo trình điều khiển undetected_chromedriver
options = uc.ChromeOptions()

# Thay đổi User-Agent để trông giống một trình duyệt người dùng thực
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")

# Thêm proxy nếu cần
options.add_argument("--proxy-server=socks5://user:pass@proxy_address:proxy_port")

# Khởi tạo trình duyệt với các thiết lập đã thêm
driver = uc.Chrome(options=options)

# Mở trang web Shopee
url = "https://shopee.vn"
driver.get(url)

# Đợi cho trang tải hoàn toàn
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
time.sleep(random.uniform(8, 12))  # Đợi ngẫu nhiên từ 8 đến 12 giây

# Tìm và điền tên đăng nhập
try:
    # Giả lập hành vi người dùng
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))
    )
    for char in "0366333953":
        username_input.send_keys(char)
        time.sleep(random.uniform(0.2, 0.5))  # Giả lập nhập từ từ

    # Tìm và điền mật khẩu
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    for char in "Vi21082004@1":
        password_input.send_keys(char)
        time.sleep(random.uniform(0.2, 0.5))

    # Tìm nút đăng nhập và nhấn vào
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='b5aVaf PVSuiZ Gqupku qz7ctP qxS7lQ Q4KP5g']"))
    )
    # Di chuyển chuột đến nút đăng nhập trước khi nhấn
    action = ActionChains(driver)
    action.move_to_element(login_button).pause(random.uniform(0.5, 1.5)).click().perform()

    print("Thực hiện đăng nhập")
    
except Exception as e:
    print(f"Lỗi: {e}")

finally:
    # Đợi một khoảng thời gian để xem kết quả đăng nhập và đóng trình duyệt
    time.sleep(10000)
    # driver.quit()
