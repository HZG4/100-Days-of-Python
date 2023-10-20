from selenium import webdriver
from selenium.webdriver.common.by import By
import time

delay = 1

#keep chrome open
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

proceed = input("Enter to proceed the game: ")
cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

