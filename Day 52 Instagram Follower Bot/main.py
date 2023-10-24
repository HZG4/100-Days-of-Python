import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time

load_dotenv('.env')
email = os.getenv('email')
password = os.getenv('password')

class InstaFollower():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        global email, password
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(email)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(password)
        button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button.click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get('https://www.instagram.com/ketosnackz/followers/')
        f_body = self.driver.find_element(By.XPATH, "//div[@class='_aano']")

        # To scroll down thrice in the followers pop-up.
        for i in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", f_body)
            time.sleep(10)

    def follow(self):
        self.follow_btns = self.driver.find_elements(By.CLASS_NAME, '_acan _acap _acas _aj1-')

        for btn in self.follow_btns:
            btn.click()
            self.find_followers()

followerbot = InstaFollower()
followerbot.login()
followerbot.find_followers()
followerbot.follow()
