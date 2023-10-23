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
    
    def tweet_at_provider(self):
        print("Post a tweet to inform about Low Speed Internet.")
        self.driver.get("https://twitter.com/i/flow/login")
        
        input("Press 'Enter' When Logged In.")

        tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        tweet_btn.click()
        txt_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span')
        txt_field.send_keys(f"@StormFiberCare Why is my internet speed {self.download_speed}mbps when I paid for 5mbps?")

        post_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
        post_btn.click()
