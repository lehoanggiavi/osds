from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

d = pd.DataFrame({"Name": [], "Year active": []})

driver = webdriver.Chrome()

url = "https://en.wikipedia.org/wiki/The_13th_Floor_Elevators"
driver.get(url)

time.sleep(3)

"Lay ten"



"Lay ngay hoat dong"
try:
    Year_active_element = driver.find_element(By.XPATH, """//th[span[contains(text(), 'Years active')]]/following-sibling::td""")
    # Year_active_element = driver.find_element(By.XPATH, "//td[contains(text(), '1965–1969, 1973, 1984, 2015')]")
    YearActive = Year_active_element.text
except:
    ""

"Tao dictionary thong tin nhac si"

musician_dict = {"Year active": YearActive}
print(musician_dict)
musician_df = pd.DataFrame([musician_dict])
print(musician_df)


"Them thong tin vao dataframe"
d = pd.concat([d, musician_df], ignore_index=True)
print(d)
