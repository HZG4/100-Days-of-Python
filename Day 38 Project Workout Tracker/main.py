import os
from datetime import datetime, date
import requests
from dotenv import load_dotenv

load_dotenv(".env")

APP_ID = os.getenv("Application_ID")
APP_KEY = os.getenv("Application_Key")
USERNAME = os.getenv("SHEETY_USERNAME")
PASSWORD = os.getenv("SHEETY_PASSWORD")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY,
    "Content-Type": "application/json"
}

params = {
 "query": input("Tell which exercise you did today?: "),
 "gender": "male",
 "weight_kg": 70.05,
 "height_cm": 179.83,
 "age": 21
}

nutritionix_response = requests.post(url=nutritionix_endpoint, headers=headers, json=params)
nutritionix_response = nutritionix_response.json()

now = datetime.now()  # Get the current date and time
Date = now.date()  # Extract the date part as a date object
Time = now.strftime("%H:%M:%S")  # Format the time as a string

sheety_endpoint = "https://api.sheety.co/7e51a67e1dbcd669b711fa9584365676/myWorkouts/workouts"

for exercise in nutritionix_response["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": str(Date),  # Convert the date to a string
            "time": Time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=sheet_inputs, auth=(USERNAME, PASSWORD))

