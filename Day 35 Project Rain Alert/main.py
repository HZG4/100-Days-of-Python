import requests
import smtplib, ssl

EMAIL = "testsubject01@gmail.com"
PASSWORD = "xxxxxxxxxxxxxxxx"

api_key = "419f9a8162033040bf175be55913db73"
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
city_name = "Sahiwal,Pk"
parameters = {"lat" : 30.66,
              "lon" : 73.11,
           "exclude": "current,minutely,daily",
            "appid" : api_key}

response = requests.get(OWM_Endpoint, params=parameters)
data = response.json()
print(data)

will_rain = False
for i in range(0, 12):
    condition_code = data['hourly'][i]['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    server = smtplib.SMTP("smtp.gmail.com", port=587)
    context = ssl.create_default_context()
    server.starttls(context=context)
    server.login(user=EMAIL, password=PASSWORD)
    server.sendmail(from_addr=EMAIL,
                    to_addrs="hamzaghafoor719@gmail.com",
                    msg="Subject: Rain Alert\n\nBring an umbrella.")
    server.quit()
