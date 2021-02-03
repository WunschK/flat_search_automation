# This is my main file


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests as r

response = r.get("https://www.openrent.co.uk/properties-to-rent/bethnal-green-greater-london?term=Bethnal%20Green,%20Greater%20London&prices_min=1000&prices_max=1500&bedrooms_min=1&bedrooms_max=2")
site = response.text
soup = BeautifulSoup(site, "html.parser")

print(soup)