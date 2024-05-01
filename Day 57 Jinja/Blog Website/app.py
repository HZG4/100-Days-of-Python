from flask import Flask, render_template
from post import Post

app = Flask(__name__)
all_posts = Post()

