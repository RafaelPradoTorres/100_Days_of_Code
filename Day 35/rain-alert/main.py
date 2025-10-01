#EXPLORE APIs
#apilist.fun

#pip install python-dotenv

#environment variables:
#os.environ.get()...
import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("C:/Python/EnvironmentVariables/.env")
api_key = os.getenv("OWM_API_KEY")
# api_key = os.environ.get("OWM_API_KEY")
# api_key = "871ada07c703d6f839f36cf03cca2023"
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = os.getenv("OWM_SID")
auth_token = os.getenv("AUTH_TOKEN")

LATITUDE = 37.927
LONGITUDE = -63.633

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()
print(response.status_code)

weather_data = response.json()
next_12_hours = weather_data["list"]

will_rain = False
for time in next_12_hours:
    condition_code = time["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid=os.getenv("MESSAGE_SID"),
        body="It's going to rain, Bring an umbrella",
        from_=os.getenv("SENDER"),
        to=os.getenv("MY_PHONE"),
    )
    print(message.status)

