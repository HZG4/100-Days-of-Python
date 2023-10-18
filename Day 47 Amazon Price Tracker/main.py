import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import smtplib
import ssl

load_dotenv(".env")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

Product_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "User-Agent": "Defined",
    "Accept-Language": "en-US,en;q=0.5"
    }

response = requests.get(url=Product_URL, headers= headers)
soup = BeautifulSoup(response.text, "lxml")

product_title = str(soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break").getText()).strip().split(',')[0]
price = float(soup.find(name= "span", class_="a-price-whole").getText())

if price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as server:
        context = ssl.create_default_context()
        server.login(user=EMAIL, password=PASSWORD)
        server.starttls(context=context)
        server.sendmail(from_addr=EMAIL,
                        to_addrs="mhamzaghafoor@gmail.com",
                        msg=f"Subject: Discount Available\n"
                            f"Product Title: {product_title}"
                            f"This Product is available for {price}")
else:
    pass