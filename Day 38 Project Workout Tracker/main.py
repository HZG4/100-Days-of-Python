import os
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