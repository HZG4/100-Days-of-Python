import pandas
import datetime
import smtplib, ssl
import os
import random

MY_EMAIL = "testsubject01@gmail.com"
PASSWORD = "jwsipukkppircyf"

today = datetime.datetime.now()

data = pandas.read_csv("birthdays.csv")
birthday_list = pandas.DataFrame(data).to_dict(orient="records")
letter_list = os.listdir("./letter_templates")

context = ssl.create_default_context()

for dict in birthday_list:
    if dict['month'] == today.month and dict['day'] == today.day:
        letter = random.choice(letter_list)
        with open(f"./letter_templates/{letter}") as file:
            wish = file.read()
            birthday_letter = wish.replace("[NAME]", dict['name'])
            print(birthday_letter)

        with smtplib.SMTP("smtp.gmail.com", port=587) as server:
            server.starttls(context=context)
            server.login(user=MY_EMAIL, password=PASSWORD)
            server.sendmail(from_addr=MY_EMAIL, to_addrs=dict['email'], msg=birthday_letter)