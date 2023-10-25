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