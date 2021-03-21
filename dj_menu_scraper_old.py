from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import csv



#1 loop going over list of links
#function appending to the df


df = pd.DataFrame({"city": [0], "rest": [0], "menu_cat": [0], "menu_item": [0], "item_price": [0]})
# this is tested on Firefox or you can use "webdriver.Chrome()"
# browser = webdriver.Chrome()
# browser.get("https://www.damejidlo.cz/")
# sleep(5)
# browser.close()

#city = "praha"
#rest = "/restaurant/l5rm/bistro-kampa"

def scrape_restaurant(city,rest):
    global df
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome()
    driver.get("https://www.damejidlo.cz" + rest)
    response = driver.page_source
    driver.quit()

    soup = BeautifulSoup(response, features="html.parser")
    r1 = soup.find("div", class_="menu__items")
    r2 = r1.find_all("li")

    result = r2


    #soup.get_text() can be used to get all the text from the tree
    for i in result:
        header = ["city", "rest", "menu_cat", "menu_item", "item_price"]
        list_raw = []
        list_raw.append(city)
        list_raw.append(rest)
        list_raw.append(i["data-menu-category"])
        list_raw.append(i.find("h3", class_="dish-name fn p-name").get_text())
        list_raw.append(i.find("div", class_="price-tags-container").get_text())
        dict_raw = dict(zip(header, list_raw))
        df = df.append(dict_raw, ignore_index=True)

#       print((i["data-object"]))

#restaurants = []
#soup_1 = soup.find("div", class_="restaurants__list").find("a", class_="hreview-aggregate url").find("href")

#find("ul", class_="vendor-list")

#for li in soup_1:
#    a =

#to extract all the lonks from the code
#for link in soup.find_all('a'):
#    restaurants.append(link.get('href'))

#print(soup_1)

#df = pd.DataFrame(restaurants)
#df.to_csv('restaurants.csv', index=False)
def open_rest_list(name_csv):
    with open(name_csv) as f:
        reader = csv.reader(f)
        data = list(reader)
        rest_list = []
    for i in data:
        for j in i:
            rest_list.append(j)
    return rest_list

for i in open_rest_list("restaurants.csv"):
    rest = i
    city = "praha"
    scrape_restaurant(city,rest)

print(df)

