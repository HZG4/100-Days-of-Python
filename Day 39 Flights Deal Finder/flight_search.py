mport requests
import os
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv(".env")
TEQUILA_ENDPOINT = os.getenv("TEQUILA_ENDPOINT")
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")

class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    