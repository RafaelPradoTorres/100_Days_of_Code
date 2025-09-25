import requests
from datetime import datetime
import smtplib

MY_LAT = -23.427320 # Your latitude
MY_LONG = -51.936958 # Your longitude

def is_iss_overhead(obj_lat, obj_lng):
    # Your position is within +5 or -5 degrees of the ISS position.
    is_lat_ok = -5 <= MY_LAT - obj_lat <= 5
    is_lng_ok = -5 <= MY_LONG - obj_lng <= 5
    return is_lat_ok and is_lng_ok

def is_dark(sun_rise, sun_set, now):
    return now <= sun_rise or now >= sun_set

def hey_lookup():
    my_email = "testerafa04@gmail.com"
    password = "bkhm ycpm uimz qnwz"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Hey!! look up!\n\nThe International Space Station is right above you!!"
                            )

    return None


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude  = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


if is_iss_overhead(iss_latitude, iss_longitude) and is_dark(sunrise, sunset, time_now):
    hey_lookup()


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



