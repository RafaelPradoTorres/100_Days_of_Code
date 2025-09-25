# api endpoint
# api request
# api paramters

import requests
from datetime import datetime

LATITUDE = -23.427320
LONGITUDE = -51.936958

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# print(longitude, latitude)
#
# #raise Exception("message")
'''
# Response codes:
httpstatuses.com
1xx: hold on
2xx: it's all good
3xx: you have no permission to access it
4xx: you did some shit
5xx: i did some shit
'''

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted":0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)
