from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Khoi tao trang web 
driver = webdriver.Chrome()

# Mo trang web can lay du lieu
url = "https://simplize.vn/co-phieu/SAB/lich-su-gia"
driver.get(url)

time.sleep(5)

# Tim tat ca the table 
table_tags = driver.find_elements(By.TAG_NAME, "table")
# for index, value in enumerate(table_tags):
#     print(f"Index: {index}, Value: {value.text}")

# Tim tat ca the tr
tr_tags = table_tags[1].find_elements(By.TAG_NAME, "tr")
# for index, value in enumerate(tr_tags):
#      print(f"Index: {index}, Value: {value.text}")


td_tags = tr_tags[1].find_elements(By.TAG_NAME, "td")
# for index, value in enumerate(td_tags):
#     print(f"Index: {index} Value: {value.text}")


# Lay tat ca cac dong trong bang
rows = driver.find_elements(By.XPATH, "//tbody[@class='simplize-table-tbody']/tr[@class='simplize-table-row simplize-table-row-level-0']")
days = []
open_prices=[]
highest_prices=[]
lowest_prices=[]
close_prices=[]
change_prices=[]
change_percent_prices=[]
volumns=[]
for row in rows: 
    # # Lay ngay giao dich
    # try:
    #     day_element = row.find_element(By.XPATH, "./td[1]/h6")
    #     day = day_element.text
    #     days.append(day)
    # except Exception as e:
    #     print(e)

    # # Lay gia mo cua
    # try:
    #     open_price_element = row.find_element(By.XPATH, "./td[2]/h6")
    #     open_price = open_price_element.text
    #     open_prices.append(open_price)
    # except Exception as e:
    #     print(e)

    # # Lay gia cao nhat
    # try:
    #     highest_price_element = row.find_element(By.XPATH, "./td[3]/h6")
    #     highest_price = highest_price_element.text
    #     highest_prices.append(highest_price)
    # except Exception as e:
    #     print(e)

    # # Lay gia thap nhat
    # try:
    #     lowest_price_element = row.find_element(By.XPATH, "./td[4]/h6")
    #     lowest_price = highest_price_element.text
    #     lowest_prices.append(lowest_price)
    # except Exception as e:
    #     print(e)

    # # Lay gia dong cua
    # try:
    #     close_price_element = row.find_element(By.XPATH, "./td[5]/h6")
    #     close_price = highest_price_element.text
    #     close_prices.append(close_price)
    # except Exception as e:
    #     print(e)

    # Lay thay doi gia
    try:
        change_price_element = row.find_element(By.XPATH, "./td[6]/h6")
        change_price = change_price_element.text
        change_prices.append(change_price)
    except Exception as e:
        print(e)

    # Lay % thay doi gia
    try:
        change_percent_price_element = row.find_element(By.XPATH, "./td[7]/div/div/h6")
        change_percent_price = change_percent_price_element.text
        change_percent_prices.append(change_percent_price)
    except Exception as e:
        print(e)

    # # Lay khoi luong
    # try:
    #     volumn_element = row.find_element(By.XPATH, "./td[8]/h6")
    #     volumn = volumn_element.text
    #     volumns.append(volumn)
    # except Exception as e:
    #     print(e)

print("Ngay mo giao dich")
print(days)
print("##############################")

print("Gia mo cua")
print(open_prices)
print("##############################")

print("Gia cao nhat")
print(highest_prices)
print("##############################")

print("Gia thap nhat")
print(lowest_prices)
print("##############################")

print("Gia dong cua")
print(close_prices)
print("##############################")

print("Thay doi gia")
print(change_prices)
print("##############################")

print("% Thay doi gia")
print(change_percent_prices)
print("##############################")

print("Khoi luong")
print(volumns)
print("##############################")

driver.quit()



