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

def check_for_upgrades():
    # find element by CSS selectors as the internal nested <b></b> changes its status from non-grayed to gray.
    store_items = driver.find_elements(By.CSS_SELECTOR, value="#store > div > b")
    prices_store = {}

    for item in store_items:
        price = item.text.replace(",", "")
        parts = price.split("-")

        if len(parts) > 1:
            key = parts[0].strip()
            value = float(parts[1].strip().replace(".", "").replace(",", "."))
            #adding an upgrade to the price_store dict
            prices_store[key] = value

    money = driver.find_element(By.ID, value="money").text
    cookie_money = float(money.replace(",", ""))

    for (key, value) in reversed(prices_store.items()):
        if cookie_money >= value:
            # find the non-grayed item and click.
            find_upgrade = driver.find_element(By.ID, value=f"buy{key}")
            find_upgrade.click()
            global delay
            delay *= 1.25
            return

timeout = time.time() + 60 * 5
check_store_time = time.time() + delay
while timeout > time.time():
    cookie.click()
    if check_store_time <= time.time():
        check_for_upgrades()
        check_store_time = time.time() + delay