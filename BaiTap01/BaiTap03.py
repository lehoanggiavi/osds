from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd



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

# for title in titles:
#     print(title)
#
# for link in links:
#     print(link)

d = pd.DataFrame({"Name": [], "Year active": []})
for link in links:
    driver.get(link)

    "Lay ten"
    try:
        # Name_element = driver.find_element(By.XPATH, "//h1[span[text()]]")
        Name_element = driver.find_element(By.XPATH, "//h1[@id='firstHeading']//span[@class='mw-page-title-main']")
        Name = Name_element.text
    except:
        ""

    "Lay ngay hoat dong"
    try:
        Year_active_element = driver.find_element(By.XPATH, """//th[span[contains(text(), 'Years active')]]/following-sibling::td""")
        # Year_active_element = driver.find_element(By.XPATH, "//td[contains(text(), '1965–1969, 1973, 1984, 2015')]")
        YearActive = Year_active_element.text
    except:
        ""

    "Tao dictionary thong tin nhac si"

    musician_dict = {"Name": Name, "Year active": YearActive}
    musician_df = pd.DataFrame([musician_dict])
    # print(musician_df)

    "Them thong tin vao dataframe"
    d = pd.concat([d, musician_df], ignore_index=True)
print(d)


# determining the name of the file
file_name = 'Musicians.xlsx'

# saving the Excel
d.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')

