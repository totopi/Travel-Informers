import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import time
from splinter import Browser
from pprint import pprint
from datetime import datetime
import pymongo
from bson.json_util import loads
import json 
import pytz


# some of the cities have odd urls on wikipedia so I manually changed them to what they are bellow
city_list = ['Vancouver', 'Portland,_Oregon', 'San Francisco', 'Seattle', 'Los Angeles', 'San Diego', 'Las Vegas', 
             'Phoenix,_Arizona', 'Albuquerque', 'Denver', 'San Antonio', 'Dallas', 'Houston', 'Kansas City', 'Minneapolis',
             'St._Louis', 'Chicago', 'Nashville', 'Indianapolis', 'Atlanta', 'Detroit', 'Jacksonville', 'Charlotte',
             'Miami', 'Pittsburgh', 'Toronto', 'Philadelphia', 'New_York_City', 'Montreal', 'Boston']

# add underscors to city names that need them
clean_city_list = []
for city in city_list:
    if ' ' in city:
        clean_city_list.append(city.replace(' ', '_'))
    else:
        clean_city_list.append(city)

print("city names prepared for wikipedia.org: \n",clean_city_list)
base_url = "https://en.wikipedia.org/wiki/"

executable_path = {'executable_path':'D:/Chromedriver/chromedriver.exe'}
browser = Browser('chrome', **executable_path)

# clear out collection before scraping
collection.delete_many({})
city_urls = {}
for city in clean_city_list:
    if collection.find_one({'city': city}):
        print(collection.find_one({'city':city}))
    else:
        record = {}
        record['city'] = city
        city_url = base_url + city
        browser.visit(city_url)
        soup = bs(browser.html, 'html.parser')

        #for title in soup.find_all("table", class_='infobox geography vcard'):
             #print(title.find_all('tr'))

        pics = []
        for pic in soup.find_all('a', class_='image'):
            img_url = 'https://en.wikipedia.org' + pic['href']
            print(img_url)
            browser.visit(img_url)
            pic_soup = bs(browser.html, 'html.parser')
            for element in pic_soup.find_all('div', class_='fullImageLink'):
                img_src = element.find('a').find('img')['src']
                pics.append(img_src)


        record['images'] = pics

        print(record)
        collection.insert_one(record)

