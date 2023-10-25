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

print('Scraping data from apartments.com .....')
# Scraping Addresses
address_soup = soup.find_all(name='div', class_="property-address js-url")
addresses = []
for address in address_soup:
    if address.getText() not in addresses:
        addresses.append(address.getText())

# Scraping Prices
price_soup = soup.find_all(name='p', class_="property-pricing")
prices = []
for price in price_soup:
    if price.getText() not in prices:
        prices.append(price.getText())

# Scraping Links
link_soup = soup.find_all(name='a', class_='property-link')
links = []
for link in link_soup:
    if link['href'] not in links:
        links.append(link['href'])

# Data Entry
print("Entering data into Google Forms .....")
for i in range(len(links)):
            driver.get(SHEETS_LINK)
            address_field = driver.find_element(By.XPATH,
                                                '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_field = driver.find_element(By.XPATH,
                                              '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field = driver.find_element(By.XPATH,
                                             '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_btn = driver.find_element(By.XPATH,
                                             '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
            address_field.send_keys(addresses[i])
            price_field.send_keys(prices[i])
            link_field.send_keys(links[i])
            submit_btn.click()
driver.close()