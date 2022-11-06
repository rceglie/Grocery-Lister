import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import regex as re
import csv
import sys
sys.path.append('../')
from sql import add_item
import time


def scrape(index):
    driver = webdriver.Chrome(executable_path='/nix/path/to/webdriver/executable')
    url = "https://www.traderjoes.com/home/products/category/food-8?filters=%7B%22page%2" + "2%3A" + str(index) + "%7D"
    # if (index > 1):
    #     url = url + "&page=" + str(index) + "&affinityOverride=default"
    driver.get(url)
    time.sleep(1.5)
    results = []
    other_results = []
    content = driver.page_source
    soup = BeautifulSoup(content)

    i = 0
    regex = re.compile('.*ProductCard.*')
    for part in soup.find_all("section", {"class" : regex}):
        i += 1
        # imag e
        image = ""
        regex2 = re.compile('.*')
        temp = part.find_all("img", {"class" : regex2})
        if (temp != []):
            image = "https://www.traderjoes.com" + temp[0]["src"]
        #print(image)


        # name
        name = ""
        regex2 = re.compile('.*ProductCard_card__title.*')
        temp = part.find_all("a", {"class" : regex2})
        if (temp != []):
            name = temp[0].text


        # price
        price = 0
        regex2 = re.compile('.*ProductPrice_productPrice__price.*')
        temp = part.find_all("span", {"class" : regex2})
        if (temp != []):
            price = float((temp[0].text)[1:])


        # url
        iurl = ""
        regex2 = re.compile('.*ProductCard_card__title.*')
        temp = part.find_all("a", {"class" : regex2})
        if (temp != []):
            iurl = "https://www.traderjoes.com" + temp[0]["href"]


        if (price > 0):
            add_item(name, price, image, iurl, 26)


for i in range(1,41):
    print("on store",i)
    scrape(i)