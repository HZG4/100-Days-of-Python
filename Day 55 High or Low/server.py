from flask import Flask
import random

num = random.randint(0, 9)
print(num)

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"