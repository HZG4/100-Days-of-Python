import time
import requests
import smtplib, ssl
from datetime import datetime

MY_LAT = 30.666121
MY_LONG = 73.102013
EMAIL = "testsubject01@gmail.com"
PASSWORD = "jwsipukkppircyf"


while True:
    time.sleep(60)
    # sunrise-sunset API request.
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

    # ISS location API request.
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #If the ISS is close to my current position
    if 20 <= iss_longitude <= 40 and 60 <= iss_latitude <= 80:

        time_now = datetime.now()
        if time_now.hour >= sunset and time_now.hour <= sunrise:

            with smtplib.SMTP('smtp.gmail.com', port=587) as server:
                context = ssl.create_default_context()
                server.starttls(context=context)
                server.login(user=EMAIL, password=PASSWORD)
                server.sendmail(from_addr=EMAIL,
                                to_addrs="hamzaghafoor719@gmail.com",
                                msg="Subject: Look up \n\nThe ISS is passing over your city.")