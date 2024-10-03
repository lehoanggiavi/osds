from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

d = pd.DataFrame({"Year active": []})

driver = webdriver.Chrome()

url = "https://en.wikipedia.org/wiki/The_13th_Floor_Elevators"
driver.get(url)

time.sleep(3)

"Lay ngay hoat dong"
# Year_active_element = driver.find_element(By.XPATH, "//td[@class = 'Years active']")
Year_active_element = driver.find_element(By.XPATH, "//th[span[contains(text(), 'Years active')]]/following-sibling::td")
YearActive = Year_active_element.text


"Tao dictionary thong tin nhac si"

musician = {"Year active": YearActive}
musician_df = pd.DataFrame([musician])

"Them thong tin va dataframe"
d = pd.concat([d, musician_df], ignore_index=True)
print(d)
