from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    number = random.randint(0, 9)
    current_year = datetime.date.today().year
    print(current_year)
    return render_template('index.html', number=number, current_year=current_year)

@app.route('/<name>')
def page(name):
    response1 = requests.get(f"https://api.genderize.io/?name={name}")
    data1 = response1.json()
    response2 = requests.get(f"https://api.agify.io?name={name}")
    data2 = response2.json()
    print(data2)
    response3 = requests.get(f"https://api.nationalize.io/?name={name}")
    data3 = response3.json()

    gender = data1["gender"]
    age = data2["age"]
    nationality = data3["country"][0]["country_id"]

    return render_template("prediction.html", name=name, age=age, gender=gender, nationality=nationality)

if __name__ == '__main__':
    app.run(debug=True)
