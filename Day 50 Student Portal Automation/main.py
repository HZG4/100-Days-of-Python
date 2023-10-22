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

for course in courses:
    course.click()

    attendance = driver.find_element(By.XPATH, '//*[@id="id_Attendance"]/a')
    attendance.click()

    course_name = driver.find_element(By.XPATH, '/html/body/div/header/div[3]/div/div[1]/h3').text.strip()
    print(f"{course_name}:")

    li_elements = driver.find_elements(By.CSS_SELECTOR, "ul.pieIDClass.legend li")
    for li in li_elements:
        label = li.find_element(By.TAG_NAME, "em").text.strip()
        value = li.find_element(By.TAG_NAME, "span").text.strip()

        print(f"{label} : {value}")

    dashboard = driver.find_element(By.XPATH, '/html/body/div/header/div[2]/div/div[2]/ul/li[1]/a')
    dashboard.click()

input("wait")