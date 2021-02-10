# This is my main file
# v0.5 Everything in main.py
# Roadmap v1.0 scraping OOP everything


import time

import requests as r
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

where = "https://www.openrent.co.uk/properties-to-rent/soho-north-west-london?term=Soho%20(north%20west),%20London&prices_min=1000&prices_max=1500&bedrooms_min=1&bedrooms_max=2"

response = r.get(where)
site = response.text
soup = BeautifulSoup(site, "html.parser")

elems = soup.select("a.pli.clearfix")

# List of all entry-links
base_address = "https://www.openrent.co.uk/"
# print(property_links)
property_links = [base_address + elem['href'] for elem in elems]

property_price_list = soup.select("div.pim.pl-title h2")
# print(property_price_list)

property_prices = [price.text.split()[0] for price in property_price_list]

# property address-list
prop_address_list = soup.select("span.banda.pt.listing-title")

property_addresses = [prop_address.text.split(",")[1] + "," + prop_address.text.split(",")[2] for prop_address in
                      prop_address_list]

# print(property_links)
# print(property_prices)
# print(property_addresses)

# Create list of dicts where each dict is one property
prop = []
for i in range(len(property_links) - 1):
    prop.append({'address': property_addresses[i], 'price': property_prices[i], 'link': property_links[i]})
    i += 1

# Selenium-stuff
chrome_driver_path = "path to chromedriver.exe"
form = "specify form link here"

options = Options()
options.add_argument('--headless');

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
driver.get(form)

for prop in prop:
    time.sleep(2)
    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address.send_keys(prop['address'])
    price.send_keys(prop['price'])
    link.send_keys(prop['link'])

    button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    button.click()
    print(prop)
    driver.get(form)

# use selenium to enter the form for each listing
