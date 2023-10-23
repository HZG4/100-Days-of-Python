from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class InternetSpeedTwitterBot():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

        self.download_speed = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go_btn = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_btn.click()
        try:
            time.sleep(30)
            self.download_speed = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
            print(f"Internet Speed: {self.download_speed}")
            return self.download_speed
        except:
            print("Took too Long to respond")
            exit()
    
    
