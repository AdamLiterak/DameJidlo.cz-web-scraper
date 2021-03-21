from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import csv

# this is tested on Firefox or you can use "webdriver.Chrome()"
# browser = webdriver.Chrome()
# browser.get("https://www.damejidlo.cz/")
# sleep(5)
# browser.close()

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome()
driver.get("https://www.damejidlo.cz/city/ceske-budejovice")
response = driver.page_source
driver.quit()

soup = BeautifulSoup(response, features="html.parser")


restaurants = []
#soup_1 = soup.find("div", class_="restaurants__list").find("a", class_="hreview-aggregate url").find("href")

#find("ul", class_="vendor-list")

#for li in soup_1:
#    a =

#to extract all the lonks from the code
for link in soup.find_all('a'):
    restaurants.append(link.get('href'))

#print(soup_1)

df = pd.DataFrame(restaurants)
df.to_csv('restaurants_ceske_budejovice.csv', index=False)