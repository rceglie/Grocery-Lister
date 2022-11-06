import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import regex as re
import csv
import sys
sys.path.append('../')
from sql import add_item


def scrape(index):
    driver = webdriver.Chrome(executable_path='/nix/path/to/webdriver/executable')
    url = "https://www.walmart.com/browse/976759?athcpid=7cbe8a0a-c5fe-4839-a851-edb3ec71638c&athpgid=AthenaContentPage&athznid=athenaModuleZone&athmtid=AthenaItemCarousel&athtvid=1&athena=true"
    if (index > 1):
        url = url + "&page=" + str(index) + "&affinityOverride=default"
    driver.get(url)
    results = []
    other_results = []
    content = driver.page_source
    soup = BeautifulSoup(content)

    regex = re.compile('.*sans-serif mid-gray relative flex flex-column w-100 hide-child-opacity.*')
    for part in soup.find_all("div", {"class" : regex}):

        # image
        image = ""
        regex2 = re.compile('.*')
        temp = part.find_all("img", {"class" : regex2})
        if (temp != []):
            image = temp[0]["src"]
        print(image)


        # name
        name = ""
        regex2 = re.compile('.*normal dark-gray mb0 mt1 lh-title f6 f5-l.*')
        temp = part.find_all("span", {"class" : regex2})
        if (temp != []):
            name = temp[0].text


        # price
        price = 0
        regex2 = re.compile('.*mr1 mr2-xl b black lh-copy f5 f4-l.*')
        temp = part.find_all("div", {"class" : regex2})
        if (temp != []):
            price = float((temp[0].text)[1:])


        # url
        iurl = ""
        regex2 = re.compile('.*absolute w-100 h-100 z-1 hide-sibling-opacity.*')
        temp = part.find_all("a", {"class" : regex2})
        if (temp != []):
            iurl = "https://www.walmart.com" + temp[0]["href"]


        if (price > 0):
            add_item(name, price, image, iurl, 25)
            print(name,price,i)

for i in range(22,25):
    print("on store",i)
    scrape(i)