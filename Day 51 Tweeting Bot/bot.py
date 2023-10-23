from selenium import webdriver

class InternetSpeedTwitterBot():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

        self.download_speed = 0
