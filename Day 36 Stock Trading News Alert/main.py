# Required libraries
import os
import requests
import ssl, smtplib
from dotenv import load_dotenv

load_dotenv(".env")

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
EMAIL = os.getenv("email")
PASSWORD = os.getenv("password")

# Alpha Vantage API Constants
AV_ENDPOINT = "https://www.alphavantage.co/query"
AV_API_KEY = os.getenv("AV_API_KEY")
AV_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "60min",
    "outputsize": "compact",
    "datatype": "json",
    "apikey": AV_API_KEY,
}

# News API Constants
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_PARAMS = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

# Get API Responses
av_response = requests.get(url=AV_ENDPOINT, params=AV_PARAMS)
av_data = av_response.json()

lastest_stock = list(av_data["Time Series (Daily)"].keys())[0]
previous_stock = list(av_data["Time Series (Daily)"].keys())[1]

lastest_stock_price = float(av_data["Time Series (Daily)"][lastest_stock]['4. close'])
previous_stock_price = float(av_data["Time Series (Daily)"][previous_stock]['4. close'])

news_response = requests.get(url=NEWS_API_ENDPOINT, params=NEWS_API_PARAMS)
news_data = news_response.json()
news = news_data['articles'][:3]

five_percent = 0.05 * previous_stock_price

# Send an email if there is 5% of increase or decrease in stock prices
if (lastest_stock_price - previous_stock_price >= five_percent) or (previous_stock_price - lastest_stock_price >= five_percent):
    context = ssl.create_default_context()
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.starttls(context=context)
    server.login(user=EMAIL, password=PASSWORD)
    for each_news in news:
        server.sendmail(from_addr=EMAIL,
                        to_addrs="mhamzaghafoor@gmail.com",
                        msg="Subject: Stock Fluctuation\n\n"
                            f"Title:{each_news['title']}\n{each_news['description']}")
else:
    print("There are no stock fluctuations")