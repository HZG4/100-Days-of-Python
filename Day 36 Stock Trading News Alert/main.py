# Required libraries
import os
import requests
import ssl, smtplib

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Alpha Vantage API Constants
AV_ENDPOINT = "https://www.alphavantage.co/query"
AV_API_KEY = os.getenv("AV_API")
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
NEWS_API_KEY = os.getenv("NEWS_API")
NEWS_API_PARAMS = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

# SMTP credentials
EMAIL = "testsubject01@gmail.com"
PASSWORD = "xxxxxxxxxxxxxx"

# Request to Alpha Vantage API and
# retrieve closing stock price of yesterday and day before yesterday.
av_response = requests.get(AV_ENDPOINT, params=AV_PARAMS)
av_response.raise_for_status()
av_data = av_response.json()
recent_date = list(av_data["Time Series (Daily)"].keys())[0]
prev_date = list(av_data["Time Series (Daily)"].keys())[1]

recent_close = round(float(av_data["Time Series (Daily)"][recent_date]["4. close"]))
prev_close = round(float(av_data["Time Series (Daily)"][prev_date]["4. close"]))


# Find out percentage change
stock_price_diff = recent_close - prev_close
percentage_change = round(stock_price_diff / prev_close * 100)

# Check whether the stock price increased/decreased by 5%
if percentage_change >= 5 or percentage_change <= -5:

    # Request to News API to retrieve first 3 news of the company
    news_api_response = requests.get(url=NEWS_API_ENDPOINT, params=NEWS_API_PARAMS)
    news_api_response.raise_for_status()
    news_api_data = news_api_response.json()

    # Retrieve first 3 news of the company
    news = [each_news for each_news in news_api_data["articles"][:3]]
    print(news)
    news_body = ""
    for msg in news:
        news_body += "".join(f"Headline: {msg['title']}\n"
                             f"Brief: {msg['description']}\n")

    server = smtplib.SMTP('smtp.gmail.com', port=587)
    context = ssl.create_default_context()
    server.starttls(context=context)
    server.login(user=EMAIL, password=PASSWORD)
    server.sendmail(from_addr=EMAIL,
                    to_addrs="hamzaghafoor719@gmail.com",
                    msg=news_body)

else:
    print("There was no significant change in the stock price.")