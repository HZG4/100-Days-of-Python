from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv('.env')

REG_NO = os.getenv("REG_NO")
PASSWORD = os.getenv("PASSWORD")

# setup driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.get("https://swl-cms.comsats.edu.pk:8082/")

# login
regno_field = driver.find_element(By.XPATH, '//*[@id="MaskedRegNo"]')
regno_field.send_keys(REG_NO)
password_field = driver.find_element(By.XPATH, '//*[@id="Password"]')
password_field.send_keys(PASSWORD)

input("Press 'Enter' after manually solving CAPTCHA.")

login_btn = driver.find_element(By.XPATH, '//*[@id="LoginSubmit"]')
login_btn.click()

dashboard = driver.find_element(By.XPATH, '//*[@id="Dash_Board"]')
dashboard.click()

courses = driver.find_elements(By.CSS_SELECTOR, "tr[onclick]")
time.sleep(2)

