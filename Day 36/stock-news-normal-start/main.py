import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv("C:/Python/EnvironmentVariables/.env")
stock_key = os.getenv("ALPHAVANTAGE_API_KEY")
news_key = os.getenv("NEWS_API_KEY")

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
'function':'TIME_SERIES_DAILY',
'symbol':STOCK_NAME,
'apikey':stock_key,
}
news_params = {
    'apiKey': news_key,
    'qInTitle': COMPANY_NAME,
}


response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data_dict = response.json()["Time Series (Daily)"]
data_list = [[item, val] for (item, val) in data_dict.items()]

yesterday_closing = float(data_list[1][1]["4. close"])

dby_closing = float(data_list[2][1]["4. close"])

diff = float(dby_closing - yesterday_closing)

up_down = None
if diff > 0:
    up_down = "📈"
else:
    up_down = "📉"

diff_percentage = (diff / yesterday_closing) * 100
print(diff_percentage)

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if abs(diff_percentage) > 0.01:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_list = news_response.json()['articles'][:3]

    mail = [f"{STOCK_NAME}: {up_down}{diff_percentage}\nHeadline: {item['title']}. \nBrief: {item['description']}\n" for item in news_list]

    account_sid = os.getenv("OWM_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    for item in news_list:
        message = client.messages.create(
            body=mail,
            from_=os.getenv("SENDER"),
            to=os.getenv("MY_PHONE"),
        )
        print(message.body)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

