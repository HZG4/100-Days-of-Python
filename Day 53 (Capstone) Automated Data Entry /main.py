from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import requests
import time
import os

load_dotenv('.env')

SHEETS_LINK = os.getenv('SHEET_LINK')
APT_LINK = os.getenv('API_LINK')

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get(APT_LINK)

wanted_location = input("Enter the location: ")
wanted_price = input('Enter the max budget for a month rent: ')
time.sleep(10)

search_home = driver.find_element(By.XPATH, '/html/body/div[1]/div/section[1]/div[1]/section/div/div/input')
search_home.send_keys(wanted_location)
time.sleep(10)
go_btn = driver.find_element(By.XPATH, '//*[@id="quickSearch"]/div/div/button').click()
time.sleep(10)

price_menu = driver.find_element(By.XPATH, '//*[@id="rentRangeLink"]')
price_menu.click()
max_price = price_menu.find_element(By.XPATH, '//*[@id="max-input"]')
max_price.send_keys(wanted_price)
max_price.send_keys(Keys.ENTER)
time.sleep(20)

# Creating soup from current url
current_url = driver.current_url
HEADERS = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'Accept-Language' : 'en-GB,en;q=0.9,ur-PK;q=0.8,ur;q=0.7,en-US;q=0.6'
}

response = requests.get(url=current_url, headers=HEADERS)
soup = BeautifulSoup(response.text, 'lxml')