import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import regex as re
import csv
import sys
sys.path.append('../')
from sql import add_item, add_store


def scrape(index):
    driver = webdriver.Chrome(executable_path='/nix/path/to/webdriver/executable')
    url = "https://www.harristeeter.com/search?fulfillment=all"
    if (index > 1):
        url = url + "&page=" + str(index)
    driver.get(url)
    results = []
    other_results = []
    content = driver.page_source
    soup = BeautifulSoup(content)

    regex = re.compile('.*ProductCard.*')
    for part in soup.find_all("div", {"class" : regex}):

        # image
        image = ""
        regex2 = re.compile('.*')
        temp = part.find_all("img", {"class" : regex2})
        if (temp != []):
            image = temp[0]["src"]


        # name
        name = ""
        regex2 = re.compile('.*')
        temp = part.find_all("h3", {"class" : regex2})
        if (temp != []):
            name = temp[0].text


        # price
        price = 0
        regex2 = re.compile('.*kds-Price-promotional-dropCaps.*')
        temp = part.find_all("span", {"class" : regex2})
        if (temp != []):
            price += int(temp[0].text)
        regex2 = re.compile('kds-Price-superscript')
        temp = part.find_all("sup", {"class" : regex2})
        if (temp != []):
            price += int(str(temp[1])[-8:-6])/100
        price = round(price, 2)


        # url
        iurl = ""
        regex2 = re.compile('.*kds-Link.*')
        temp = part.find_all("a", {"class" : regex2})
        if (temp != []):
            iurl = "https://www.harristeeter.com/" + temp[0]["href"]


        #add_item(name, price, image, iurl, 23)
        if (price > 0):
            add_item(name, price, image, iurl, 23)
            print(name,price)


for i in range(10,12):
    print("on store",i)
    scrape(i)